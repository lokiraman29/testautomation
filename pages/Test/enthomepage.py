# EbHomePage.py
from playwright.sync_api import Page, expect
import os

class EbHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.firstname = page.locator("[name='FirstName']")
        self.lastname = page.locator("[name='LastName']")
        self.email = page.locator("[name='Email']")
        self.contactnumber = page.locator("[name='MobilePhone']")
        self.companyname = page.locator("[name='Company']")
        self.jobtitle = page.locator("[name='Title']")
        self.submit = page.locator("button[type='submit']")

        #if not os.path.exists("screenshots"):
           # os.makedirs("screenshots")

    # <-- Rename this method
    def goto_url(self, url: str):
        self.page.goto(url)
        expect(self.page).to_have_url(url)

    def fill_contact_form(
        self,
        firstname: str,
        lastname: str,
        email: str,
        contactnumber: str,
        companyname: str,
        jobtitle: str
    ):
        self.firstname.fill(firstname)
        self.lastname.fill(lastname)
        self.email.fill(email)
        self.contactnumber.fill(contactnumber)
        self.companyname.fill(companyname)
        self.jobtitle.fill(jobtitle)

    def submit_click(self):
        expect(self.submit).to_be_visible()
        self.submit.click()

    def take_screenshot(self, filename: str):
        path = f"screenshots/{filename}.png"
        self.page.screenshot(path=path, full_page=True)
        print(f"Screenshot saved: {path}")
