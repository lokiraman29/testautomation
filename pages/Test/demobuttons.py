from playwright.sync_api import Page, Expect, expect
class demobuttons:
    def __init__(self,page:Page):
        self.page=page
        self.clickme=page.locator("[class=\"btn btn-primary\"]")
        


    def gotourl(self,url:str):
        self.page.goto(url)
    def clickme_click(self):
        self.clickme.click()