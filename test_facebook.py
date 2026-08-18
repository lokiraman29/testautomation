# #from playwright.sync_api import Page, Expect, expect
# #class pwa_login_page:
#     #def init(self,page:Page):
#         #self.page = page
        
#         # FIX: Use generic locators to find the input fields reliably
#         # Assuming the first text/email input is the username field
#         self.username = page.locator('input[type="text"], input[type="email"]').first
#         self.password = page.locator("input[type=\"password\"]")
        
#         # FIX: Use the most robust button locator
#         self.loginbutton = page.get_by_role("button", name="Login") 
        
#     def pwa_login(self,username:str,password:str):
        
#         # FIX: Explicitly wait for the username field to be visible before filling
#         self.username.wait_for(state="visible", timeout=10000)
        
#         self.username.fill(username)  
#         self.password.fill(password)
        
#         # FIX: Use expect to wait for the button to be enabled before clicking
#         expect(self.loginbutton).to_be_enabled(timeout=5000)
#         self.loginbutton.click()






import pytest
from playwright.sync_api import sync_playwright
from pages.Test.facebookloginpage import facebookloginpage
@pytest.mark.smoketest 
def test_facebook():
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        loginpage=facebookloginpage(page)
        loginpage.gotourl("https://www.facebook.com/")
        loginpage.createnewaccount_click()
        loginpage.createnewaccount_action("test","facebook","2","5","1993","9546211223")
        loginpage.browsernavigation()
        page.pause()

#         page.goto("https://demoqa.com/automation-practice-form")

#         page.get_by_role("textbox", name="First Name").fill("Loke")
#         page.get_by_role("textbox", name="Last Name").fill("test")
#         page.get_by_role("textbox", name="name@example.com").fill("test@gmail.com")
#         #check box, radio box ->type=radio, type=checkbox
#         page.getByText("textbox", name="Full Name").check()
#         page.wait_for_timeout(5000)
#         browser.close()


        
