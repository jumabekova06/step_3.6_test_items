class Testitems:
    def test_items(self, browser):
        browser.find_element_by_css_selector(".btn-add-to-basket").click()
        success_button = browser.find_element_by_css_selector('.alert-success')
        assert success_button

