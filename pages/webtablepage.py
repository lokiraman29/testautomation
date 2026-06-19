from playwright.sync_api import Page, expect


class webtablepage:

    def __init__(self, page: Page):
        self.page = page
        self.add = page.locator('id=addNewRecordButton')
        self.firstname = page.locator('id=firstName')
        self.lastname = page.locator('id=lastName')
        self.email = page.locator('id=userEmail')
        self.age = page.locator('id=age')
        self.salary = page.locator('id=salary')
        self.department = page.locator('id=department')
        self.submit = page.locator('id=submit')

    def gotourl(self, url: str):
        self.page.goto(url)


    def webtablepageone(self, firstname: str, lastname: str, email: str, age: str, salary: str, department: str):
        self.add.click()