from playwright.sync_api import Page, expect


class linkpage:

    def __init__(self, page: Page):
        self.page = page
        self.home = page.locator('#simpleLink')
        self.dynamic_home = page.locator("#dynamicLink")
        self.noContent = page.locator("#no-content")
        self.moved = page.locator("#moved")
        self.badRequest = page.locator("#bad-request")
        self.unauthorized = page.locator("#unauthorized")
        self.forbidden = page.locator("#forbidden")
        self.notFound = page.locator("#invalid-url")    
        self.link_response = page.locator("#linkResponse")

    def gotourl(self, url: str):
        self.page.goto(url)

    def click_link_that_opens_new_page(self, link):
        with self.page.context.expect_page() as new_page_info:
            link.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        expect(new_page).to_have_url("https://demoqa.com/")
        new_page.wait_for_timeout(3000)
        new_page.close()

    def click_api_link_and_print_message(self, link):
        link.click()
        expect(self.link_response).to_be_visible()
        message = self.link_response.inner_text()
        self.link_response.evaluate(
            """element => {
                element.style.backgroundColor = "yellow";
                element.style.border = "3px solid red";
                element.style.padding = "8px";
            }"""
        )
        self.page.wait_for_timeout(1500)
        self.link_response.evaluate(
            """element => {
                element.style.backgroundColor = "";
                element.style.border = "";
                element.style.padding = "";
            }"""
        )
        print(message)

    def linkspageone(self):
        self.click_link_that_opens_new_page(self.home)
        self.click_link_that_opens_new_page(self.dynamic_home)
        self.click_api_link_and_print_message(self.noContent)
        self.click_api_link_and_print_message(self.moved)
        self.click_api_link_and_print_message(self.badRequest)
        self.click_api_link_and_print_message(self.unauthorized)
        self.click_api_link_and_print_message(self.forbidden)
        self.click_api_link_and_print_message(self.notFound)
