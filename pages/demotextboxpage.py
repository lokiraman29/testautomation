from playwright.sync_api import Page, expect


class demotextboxpage:

    def __init__(self, page: Page):
        self.page = page
        self.fullname = page.locator('[id="userName"]')
        self.email = page.locator('[id="userEmail"]')
        self.currentaddress = page.locator('[id="currentAddress"]')
        self.permanentaddress = page.locator('[id="permanentAddress"]')
        self.submit = page.locator('[id="submit"]') 

    def gotourl(self, url: str):
        self.page.goto(url)

    def demotextboxpageone(
        self,
        fullname: str,
        email: str,
        currentaddress: str,
        permanentaddress: str,
    ):
        self.fullname.fill(fullname)
        self.email.fill(email)
        self.currentaddress.fill(currentaddress)
        self.permanentaddress.fill(permanentaddress)
        self.submit.click() 
        
