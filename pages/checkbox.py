from playwright.sync_api import Page, expect


class checkbox:

    def __init__(self, page: Page):
        self.page = page
        self.home_expand_button = page.locator(".rc-tree-switcher")
        self.desktop_checkbox = page.get_by_label("Select Desktop")
        self.documents_checkbox = page.get_by_label("Select Documents")
        self.downloads_checkbox = page.get_by_label("Select Downloads")

    def gotourl(self, url: str):
        self.page.goto(url) 

    def checkboxpage(self):
        self.home_expand_button.click()
        self.desktop_checkbox.click()
        self.documents_checkbox.click()
        self.downloads_checkbox.click()
