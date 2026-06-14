from playwright.sync_api import Page


class DemoQAFormPage:
    def __init__(self, page: Page):
        self.page = page
        self.firstname = page.locator("#firstName")
        self.lastname = page.locator("#lastName")
        self.email = page.locator("#userEmail")
        self.mobile = page.locator("#userNumber")
        self.dateofbirth = page.locator("#dateOfBirthInput")
        self.date_month = page.locator(".react-datepicker__month-select")
        self.date_year = page.locator(".react-datepicker__year-select")
        self.subjects = page.locator("#subjectsInput")
        self.picture = page.locator("#uploadPicture")
        self.currentaddress = page.locator("#currentAddress")
        self.submit = page.locator("#submit")

    def gotourl(self, url: str):
        self.page.goto(url)

    def select_gender(self, gender: str):
        gender_ids = {
            "Male": "gender-radio-1",
            "Female": "gender-radio-2",
            "Other": "gender-radio-3",
        }
        self.page.locator(f'#{gender_ids[gender]}').check(force=True)

    def select_date_of_birth(self, day: str, month: str, year: str):
        self.dateofbirth.click()
        self.date_year.select_option(year)
        self.date_month.select_option(label=month)
        self.page.locator(
            f".react-datepicker__day--0{int(day):02d}:not(.react-datepicker__day--outside-month)"
        ).click()

    def select_hobby(self, hobby: str):
        hobby_ids = {
            "Sports": "hobbies-checkbox-1",
            "Reading": "hobbies-checkbox-2",
            "Music": "hobbies-checkbox-3",
        }
        self.page.locator(f'#{hobby_ids[hobby]}').check(force=True)

    def submit_student_details(self, student: dict):
        self.firstname.fill(student["first_name"])
        self.lastname.fill(student["last_name"])
        self.email.fill(student["email"])
        self.select_gender(student["gender"])
        self.mobile.fill(student["mobile"])
        self.select_date_of_birth(
            student["birth_day"],
            student["birth_month"],
            student["birth_year"],
        )
        self.subjects.fill(student["subject"])
        self.subjects.press("Enter")
        self.select_hobby(student["hobby"])
        self.picture.set_input_files(student["upload_file"])
        self.currentaddress.fill(student["current_address"])
        self.submit.click()
