from playwright.sync_api import Page


class demobuttonspage:

    def __init__(self, page: Page):
        self.page = page
        self.doubleclickme = page.locator("#doubleClickBtn")
        self.rightclickme = page.locator("#rightClickBtn")
        self.clickme = page.get_by_role("button", name="Click Me", exact=True)

    def gotourl(self, url: str):
        self.page.goto(url)

    def demobuttonsmethod(self):
        self.doubleclickme.dblclick()
        self.rightclickme.click(button="right")
        self.clickme.click()
