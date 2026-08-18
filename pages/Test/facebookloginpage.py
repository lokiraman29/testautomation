from playwright.sync_api import Page, Expect, expect
class facebookloginpage:
    def __init__(self,page:Page):
        self.page=page
        self.createnewaccount=page.locator("[data-testid=\"open-registration-form-button\"]")
        self.login=page.locator("[data-testid=\"royal-login-button\"]")
        self.firstname=page.locator("[name=\"firstname\"]")
        self.lastname=page.locator("[name=\"lastname\"]")
        self.date=page.locator("[name=\"birthday_day\"]")
        self.month=page.locator("[name=\"birthday_month\"]")
        self.year=page.locator("[name=\"birthday_year\"]")
        self.female=page.locator("[value=\"1\"][name=\"sex\"]")
        self.mobile=page.locator("[name=\"reg_email__\"]")


    def gotourl(self,url:str):
        #self.page.pause()
        self.page.goto(url)
        expect(self.page).to_have_url(url)
       # expect(self.page).to_have_title("Facebook – log in or ")
    def createnewaccount_click(self):
        expect(self.createnewaccount).to_be_visible()
        expect(self.createnewaccount).to_be_enabled()
        text=self.createnewaccount.text_content()
        print(text)
        print("helllo")
        self.createnewaccount.click()
    def createnewaccount_action(self,firstname:str, lastname:str,Date:str,Month:str,Year:str,Mobile:str):
        self.firstname.fill(firstname)
        self.lastname.fill(lastname)
        self.date.select_option(Date)
        self.month.select_option(Month)
        self.year.select_option(Year)
        self.female.click()
        self.mobile.fill(Mobile)



    def browsernavigation(self):
        self.page.go_back()
        self.page.go_forward()
        self.page.reload()
        
    



        