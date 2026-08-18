from playwright.sync_api import Page, Expect, expect
class alert:
    def __init__(self,page:Page):
        self.page=page
        self.clickme=page.locator("[id=\"alertButton\"]")
        self.clickme2=page.locator("[id=\"confirmButton\"]")
        self.click3=page.locator("[id=\"promtButton\"]")  
    def handle_alerts(self):
        self.page.once("dialog",lambda d: d.accept("testing"))
        self.page.pause()
        self.click3.click()

    