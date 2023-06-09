import re
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class LoginTest(FunctionalTest):
    def test_can_get_email_link_to_log_in(self):
        # Edith goes to the superlists site
        # and notices a "Log in" section in the navbar for the first time
        # It's telling her to enter her email address, so she does
        if self.staging_server:
            test_email = "18ahewson@gmail.com"
        else:
            test_email = "edith@example.com"

        self.browser.get(self.live_server_url)
        self.browser.find_element(by="id", value="id_login_button").click()
        self.browser.find_element("name", "email").send_keys(test_email)
        self.browser.find_element("name", "email").send_keys(Keys.ENTER)

        # A message appears telling her an email has been sent
        self.wait_for(
            lambda: self.assertIn(
                "Check your email", self.browser.find_element("tag name", "body").text
            )
        )

        # She checks her email and finds a message
        body = self.wait_for_email(test_email, self.subject)
        # It has a URL link in it
        self.assertIn("Here's your personal login link:", body)
        url_search = re.search(r"http://.+/.+$", body, re.M)
        if not url_search:
            self.fail(f"Could not find url in email body:\n{body}")
        url = url_search.group(0)
        self.assertIn(self.live_server_url, url)

        # she clicks it
        self.browser.get(url)

        # she is logged in!
        self.wait_to_be_logged_in(email=test_email)

        # Now she logs out
        self.browser.find_element(by="link text", value="Logout").click()

        # She is logged out
        self.wait_to_be_logged_out(email=test_email)
        self.browser.find_element("name", "email")
