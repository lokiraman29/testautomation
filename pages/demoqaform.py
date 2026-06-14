from playwright.sync_api import Page, expect


class demoqaform:
    def __init__(self, page: Page):
        self.page = page
        self.firstname = page.locator("#firstName")
        self.lastname = page.locator("#lastName")
        self.email = page.locator("#userEmail")
        self.gender_female = page.locator('[id="gender-radio-2"]')
        self.mobile = page.locator('[id="userNumber"]')
        self.dateofbirth = page.locator('[id="dateOfBirthInput"]')
        self.date_month = page.locator(".react-datepicker__month-select")
        self.date_year = page.locator(".react-datepicker__year-select")
        self.date_day_11 = page.locator(
            ".react-datepicker__day--011:not(.react-datepicker__day--outside-month)"
        )
        self.subjects = page.locator('[id="subjectsInput"]')
        self.hobbies_sports = page.locator('[id="hobbies-checkbox-1"]')
        self.picture = page.locator('[id="uploadPicture"]')
        self.currentaddress = page.locator('[id="currentAddress"]')
        self.state = page.locator('[id="react-select-3-input"]')
        self.city = page.locator('[id="react-select-4-input"]') 
        self.submit = page.locator('[id="submit"]')                                           


    def gotourl(self, url: str):
        self.page.goto(url)

    def select_date_of_birth(self):
        self.dateofbirth.click()
        self.date_year.select_option("2002")
        self.date_month.select_option("11")
        #self.date_day_11.click()

    def demoqaformpage(self, firstname: str, lastname: str, email: str, mobile: str, 
                       subjects: str, hobbies: str, currentaddress: str):
        self.firstname.fill(firstname)
        self.lastname.fill(lastname)
        self.email.fill(email)
        self.gender_female.check(force=True)
        self.mobile.fill(mobile)
        self.select_date_of_birth()
        self.subjects.fill(subjects)
        self.subjects.press("Enter")
        self.hobbies_sports.check(force=True)
        self.currentaddress.fill(currentaddress)
        self.submit.click() 
