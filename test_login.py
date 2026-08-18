import pytest
from playwright.sync_api import sync_playwright, expect


def test_login():
    with sync_playwright as p:
        browser=p.chromium.launch()
        context=browser.new_context()
        page=context.new_page()

        # Action: Lauching the URL ->.goto
        page.goto("https://demoqa.com/buttons")

        #Click -> .click()
        page.get_by_role("button", name="Click Me", exact=True).click()
        page.get_by_role("button", name="Double Click Me").dblclick()
        page.get_by_role("button", name="Right Click Me").click(button="right")

        #Textbox
        # type/fill the content, clear

        page.get_by_role("textbox", name="Full Name").fill("Loke")   
        page.get_by_role("textbox", name="Full Name").clear();     
        

        #check box, radio box ->type=radio, type=checkbox
        page.get_by_role("textbox", name="Full Name").check()

        #dropdown <select -> select_option
        page.locator("[id=\"day\"]").select_option("9")

        #keyboard action, shortcuts .press
        page.get_by_role("textbox", name="Full Name").click()
        page.get_by_role("textbox", name="Full Name").press("Control+Alt+Delete")

        #upload: set_input_files("relative")
        page.get_by_role("button", name="Select a file").set_input_files(['api_tests/load_cookies.py', 'api_tests/load_cookies.py'])

        # click
        download_info=page.get_by_role("link", name="Download").click();
        download=download_info.value

        # rename
        #save
        download.save_as("downloads/xccc.pdf")

        #drag and drop
        page.locator("Source").drag_to(page.locator("destionation"))
        page.locator("source").hover()
        page.mouse.down()
        page.locator("destination").hover()
        page.mouse.up()



#@pytest.mark.demoqa
def test_demoqa_mouse_keyboard_headed():
    with sync_playwright() as p:
        # Launch browser in headed mode
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        # Step 1: Go to the DemoQA homepage
        page.goto("https://demoqa.com/")
        page.mouse.wheel(0, 1000)
        page.get_by_text("Elements").click()
        expect(page).to_have_url("https://demoqa.com/elements")

        # Step 2: Keyboard typing and key events
        page.goto("https://demoqa.com/text-box")

        page.fill("#userName", "Playwright Tester")
        page.fill("#userEmail", "tester@demoqa.com")

       # Focus and type using keyboard
        address_field = page.locator("#currentAddress")
        address_field.click()
        page.keyboard.type("123 Automation Street, Test City", delay=100)

        # Select and copy text (simulate with clipboard API)
        copied_text = address_field.input_value()
        page.evaluate(f"navigator.clipboard.writeText('{copied_text}')")

        # Move to permanent address and paste
        permanent_field = page.locator("#permanentAddress")
        permanent_field.click()

        # Read clipboard and paste its contents
        paste_text = page.evaluate("navigator.clipboard.readText()")
        page.keyboard.type(paste_text, delay=100)

        # Submit form using keyboard
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")
        expect(page.locator("#output")).to_be_visible()
        page.pause();