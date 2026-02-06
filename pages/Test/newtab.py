from playwright.sync_api import Page, Expect, expect
class pwa_newtab:
    def __init__(self,page:Page):
        self.page = page
        self.newtab=page.locator("[id=\"tabButton\"]")
        self.newwindow=page.locator("[id=\"windowButton\"]")

    def click_newtab(self):
        with self.page.context.expect_page() as new_page_window:
            self.newtab.click()
            page1=new_page_window.value
            return page1
                                 
                                 