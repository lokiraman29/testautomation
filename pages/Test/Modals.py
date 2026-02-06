from playwright.sync_api import Page, Expect, expect
class Modals:
    def __init__(self,page:Page):
        self.page=page
        self.smallmodal=page.locator("[id=\"showSmallModal\"]")
          
    def handle_modals(self):
        #self.page.once("dialog",lambda d: d.accept("testing"))
        self.page.pause()
        self.smallmodal.click()