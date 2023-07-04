import os
import poplib
import re
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.firefox.options import Options
from django.core import mail

MAX_WAIT = 10


def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    return modified_fn


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.staging_server = os.environ.get("STAGING_SERVER")
        if self.staging_server:
            self.live_server_url = "http://" + self.staging_server
            self.test_email = "18ahewson@gmail.com"
        else:
            self.test_email = "edith@example.com"
        self.subject = "Your login link for Superlists"

    def tearDown(self) -> None:
        self.browser.quit()

    def quick_login(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(by="id", value="id_login_button").click()
        self.browser.find_element("name", "email").send_keys(self.test_email)
        self.browser.find_element("name", "email").send_keys(Keys.ENTER)
        self.wait_for(
            lambda: self.assertIn(
                "Check your email", self.browser.find_element("tag name", "body").text
            )
        )
        body = self.wait_for_email(self.test_email, self.subject)
        url_search = re.search(r"http://.+/.+$", body)
        if not url_search:
            self.fail(f"Could not find url in email body:\n{body}")
        url = url_search.group(0)
        self.browser.get(url)

    def get_item_input_box(self):
        return self.browser.find_element(by="id", value="id_text")

    @wait
    def wait_for(self, fn):
        return fn()

    @wait
    def wait_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(by="id", value="id_list_table")
        rows = table.find_elements(by="tag name", value="tr")
        self.assertIn(row_text, [row.text for row in rows])

    @wait
    def wait_to_be_logged_in(self, email):
        self.browser.find_element("link text", "Logout")
        navbar = self.browser.find_element("css selector", ".navbar")
        self.assertIn(email, navbar.text)

    @wait
    def wait_to_be_logged_out(self, email):
        self.browser.find_element(by="name", value="email")
        navbar = self.browser.find_element(by="css selector", value=".navbar")
        self.assertNotIn(email, navbar.text)

    def add_list_item(self, item_text):
        num_rows = len(
            self.browser.find_elements(by="css selector", value="#id_list_table tr")
        )
        self.get_item_input_box().send_keys(item_text)
        self.get_item_input_box().send_keys(Keys.ENTER)
        item_number = num_rows + 1
        self.wait_for_row_in_list_table(f"{item_number}: {item_text}")

    def wait_for_email(self, test_email, subject):
        if not self.staging_server:
            email = mail.outbox[0]
            self.assertIn(test_email, email.to)
            self.assertEqual(email.subject, subject)
            return email.body

        email_id = None
        start = time.time()
        inbox = poplib.POP3_SSL("pop.gmail.com")
        try:
            inbox.user(test_email)
            inbox.pass_(os.environ["EMAIL_PASSWORD"])
            while time.time() - start < 60:
                # get 10 newest messages
                count, _ = inbox.stat()
                for i in reversed(range(max(1, count - 10), count + 1)):
                    print("getting msg", i)
                    _, lines, __ = inbox.retr(i)
                    lines = [l.decode("utf8") for l in lines]
                    print(lines)
                    if f"Subject: {subject}" in lines:
                        email_id = i
                        body = "\n".join(lines)
                        return body
                    time.sleep(5)
        finally:
            if email_id:
                inbox.dele(email_id)
            inbox.quit()
