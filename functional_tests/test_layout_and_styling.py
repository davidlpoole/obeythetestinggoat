from unittest import skip

from selenium.webdriver import Keys

from functional_tests.base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    @skip
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centred
        input_box = self.get_item_input_box()
        self.assertAlmostEqual(
            input_box.location["x"] + input_box.size["width"] / 2, 512, delta=20
        )

        # She starts a new list and sees the input is nicely
        # centered there too
        input_box.send_keys("testing")
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: testing")
        input_box = self.get_item_input_box()
        self.assertAlmostEqual(
            input_box.location["x"] + input_box.size["width"] / 2, 512, delta=20
        )
