from playwright.sync_api import sync_playwright

from pages.Businesssimpage import Businesssimpage


def test_mobile_sim_plans():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        business_page = Businesssimpage(page)
        business_page.gotourl("https://www.optus.com.au/")
        business_page.click_mobile_sim_plans()
        browser.close()
