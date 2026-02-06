from playwright.sync_api import Page, Expect, expect
class frames:
    def __init__(self,page:Page):
        self.page=page
        self.clickme=page.frame_locator("[id=\"frame1\"]").get_by_role("heading", name="This is a sample page")


   
    def clickme_click(self):
        self.clickme.click()

