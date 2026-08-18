import pytest
from playwright.sync_api import sync_playwright
from pages.Test.enthomepage import EbHomePage
from utils.csv_reader import csvreader

# List of pages with the form
# urls = [
#     "https://www.optus.com.au/enterprise/contact-us",
#     "https://www.optus.com.au/enterprise/industries/construction",
#     "https://www.optus.com.au/enterprise/industries/education",
#     "https://www.optus.com.au/enterprise/industries/property",
#     "https://www.optus.com.au/enterprise/industries/retail",
#     "https://www.optus.com.au/enterprise/industries/transport-logistics",
#     "https://www.optus.com.au/enterprise/industries/manufacturing",
#     "https://www.optus.com.au/enterprise/industries/financial-services-insurance",
#     "https://www.optus.com.au/enterprise/industries/professional-services",
#     "https://www.optus.com.au/enterprise/industries/energy-utilities",
#     "https://www.optus.com.au/enterprise/industries/health-care-aged-care-social-services",
#     "https://www.optus.com.au/enterprise/industries/mining-resources",
#     "https://www.optus.com.au/enterprise/industries/not-for-profit-community-services"

# ]

# # Form data
# form_data = {
#     "firstname": "Test",
#     "lastname": "Facebook",
#     "email": "test@yop.com",
#     "contactnumber": "0456211336",
#     "companyname": "Test Company",
#     "jobtitle": "Mr"
# }

#@pytest.mark.parametrize("url", urls)#
def test_ebhome_form_submission():
    """Test form submission on multiple pages (one page per test)."""
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        #datas=csvreader.get_row("testdata/data.csv")
        #datas=csvreader.get_row("testdata/data.csv",rows=[0,2])
        datas=csvreader.get_row("testdata/data.csv",rows=[1])
        # Initialize page object
        
        for data in datas:
            home = EbHomePage(page)

        # Go to the page
            home.goto_url(data["url"])

        # Fill the form
            home.fill_contact_form(data["firstname"],data["lastname"],data["email"],data["contactnumber"],data["companyname"],data["jobtitle"])

        # Submit the form
            home.submit_click()

        # Take a screenshot for this page
            filename = data["url"].split("/")[-1] or "contact-us"
            home.take_screenshot(f"eb_{filename}")

        # Close browser
        browser.close()
