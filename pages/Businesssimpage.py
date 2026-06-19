from playwright.sync_api import Page


class Businesssimpage:

    def __init__(self, page: Page):
        self.page = page
        self.mobile_meganav = page.get_by_role("button", name="Mobile", exact=True)
        self.internet_meganav = page.get_by_role("button", name="Internet", exact=True)
        self.tablets_meganav = page.get_by_role(
            "button", name="Tablets & Watches", exact=True
        )
        self.accessories_meganav = page.get_by_role("button", name="Accessories", exact=True)
        self.network_meganav = page.get_by_role("button", name="Network", exact=True)
        self.sim_plans = page.get_by_role(
            "link", name="Explore SIM plans", exact=True
        )
        self.small_plan = page.get_by_test_id("select-cta-0")
        self.new_customer = page.locator(
            'input[name="dwfrm_customerIntent_customerStatus"][value="new"]'
        )
        self.continue_button = page.get_by_role("button", name="Continue")
        self.esim = page.locator('input[type="radio"][value="ESIM"]')
        self.checkout_button = page.get_by_role("button", name="Checkout", exact=True)
        self.email_address = page.get_by_label("Email address", exact=True)
        self.confirm_email_address = page.get_by_label(
            "Confirm email address", exact=True
        )
        self.continue_button_checkout = page.get_by_role("button", name="Continue", exact=True)
        self.personal_details_continue_button = page.get_by_role(
            "button", name="Continue", exact=True
        )
        self.first_name = page.get_by_label("First name", exact=True)
        self.last_name = page.get_by_label("Last name", exact=True)
        self.date_of_birth = page.get_by_label("Date of birth", exact=True)
        self.mobile_number = page.get_by_label("Mobile number", exact=True)
        self.address_line_1 = page.get_by_label("Address line 1", exact=True)
        self.suburb = page.get_by_label("Suburb", exact=True)

    def gotourl(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def click_all_meganav_items(self):
        self.mobile_meganav.click()
        self.page.wait_for_timeout(2000)
        self.internet_meganav.click()
        self.page.wait_for_timeout(2000)
        self.tablets_meganav.click()
        self.page.wait_for_timeout(2000)
        self.accessories_meganav.click()
        self.page.wait_for_timeout(2000)
        self.network_meganav.click()
        self.page.wait_for_timeout(2000)

    def click_mobile_sim_plans(self):
        self.mobile_meganav.click()
        self.page.wait_for_timeout(1000)
        self.sim_plans.evaluate("link => link.click()")
        self.page.wait_for_url("**/mobile/plans/shop**", wait_until="domcontentloaded")
        self.page.wait_for_timeout(2000)
        self.small_plan.click()
        self.page.wait_for_url(
            "https://shop.optus.com.au/customer-type**",
            wait_until="domcontentloaded",
        )
        self.new_customer.check(force=True)
        self.continue_button.click()
        self.page.wait_for_url(
            "**/product-options/**stage=SIM**",
            wait_until="domcontentloaded",
        )
        self.esim.check(force=True)
        self.continue_button.click()
