import pytest
from playwright.sync_api import sync_playwright
from pages.Test.enthomepage import EbHomePage
from utils.excelreader import excelreader
@pytest.mark.parametrize("data", excelreader.get_row("testdata/data.xlsx","Sheet1",rows=[4,5,7]))
def test_ebhome_form1_submission(data):
    """Test form submission on multiple pages (one page per test)."""
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        #page.pause()
        #datas=csvreader.get_row("testdata/data.csv")
        #datas=excelreader.get_row("testdata/data.xlsx","Sheet1",rows=[4,5,7])
        #datas=excelreader.get_row("testdata/data.xlsx",rows=[1])
        # Initialize page object
        
        home = EbHomePage(page)
        # Go to the page
        home.goto_url(data["url"])

        # Fill the form
        home.fill_contact_form(data["firstname"],data["lastname"],data["workemail"],data["contactnumber"],data["companyname"],data["jobtitle"])

        # Submit the form
        home.submit_click()

        # Take a screenshot for this page
        filename = data["url"].split("/")[-1] or "contact-us"
        home.take_screenshot(f"eb_{filename}")

        # Close browser
        browser.close()
