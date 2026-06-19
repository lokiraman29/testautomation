from playwright.sync_api import Page, expect


class radiobuttonpage:

    def __init__(self, page: Page):
        self.page = page
        self.impressive = page.locator("id=impressiveRadio")

    def gotourl(self, url: str):
        self.page.goto(url)

    def radiobuttonpageone(self):
        self.impressive.click()
