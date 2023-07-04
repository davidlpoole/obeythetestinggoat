from selenium import webdriver
from .base import FunctionalTest


def quit_if_possible(browser):
    try:
        browser.quit()
    except:
        pass


class SharingTest(FunctionalTest):
    # Edith is a logged-in user
    def test_can_share_a_list_with_another_user(self):
        self.browser.get(self.live_server_url)
        self.wait_to_be_logged_out(self.test_email)
        self.quick_login()
        self.wait_to_be_logged_in(self.test_email)
