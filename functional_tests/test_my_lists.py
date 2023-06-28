import re
from unittest import skip

from django.conf import settings
from django.contrib.auth import get_user_model, SESSION_KEY, BACKEND_SESSION_KEY
from django.contrib.sessions.backends.db import SessionStore
from selenium.webdriver import Keys

from functional_tests.base import FunctionalTest

User = get_user_model()


class MyListTest(FunctionalTest):
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

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Edith is a logged-in user
        self.browser.get(self.live_server_url)
        self.wait_to_be_logged_out(self.test_email)
        self.quick_login()
        self.wait_to_be_logged_in(self.test_email)

        # She goes to the home page and starts a list
        self.add_list_item("Reticulate splines")
        self.add_list_item("Immanentize eschaton")
        first_list_url = self.browser.current_url

        # She notices a "My lists" link, for the first time.
        self.browser.find_element(by="link text", value="My lists").click()

        # She sees that her list is in there, named according to its
        # first list item
        self.wait_for(
            lambda: self.browser.find_element(
                by="link text", value="Reticulate splines"
            )
        )
        self.browser.find_element(by="link text", value="Reticulate splines").click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
        )

        # She decides to start another list, just to see
        self.browser.get(self.live_server_url)
        self.add_list_item("Click cows")
        second_list_url = self.browser.current_url

        # Under "My lists", her new list appears
        self.browser.find_element(by="link text", value="My lists").click()
        self.wait_for(
            lambda: self.browser.find_element(by="link text", value="Click cows")
        )
        self.browser.find_element(by="link text", value="Click cows").click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )

        # She logs out. The "My lists" option disappears
        self.browser.find_element(by="link text", value="Logout").click()
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_elements(by="link text", value="My lists"), []
            )
        )
