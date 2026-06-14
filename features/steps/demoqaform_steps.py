from pathlib import Path

from behave import given, then, when
from openpyxl import load_workbook
from playwright.sync_api import expect

from libraries.demoqaform_page import DemoQAFormPage


EXCEL_FILE = Path("/Users/lokeraman/Desktop/submit form details/student_details.xlsx")


def read_student_from_excel():
    workbook = load_workbook(EXCEL_FILE, data_only=True)
    sheet = workbook["student_details"]
    headers = [cell.value for cell in sheet[1]]
    values = [cell.value for cell in sheet[2]]
    workbook.close()
    return {
        header: "" if value is None else str(value)
        for header, value in zip(headers, values)
    }


@given("I open the DemoQA practice form")
def open_demoqa_practice_form(context):
    context.demoqa_form = DemoQAFormPage(context.page)
    context.demoqa_form.gotourl("https://demoqa.com/automation-practice-form/")


@when("I submit the form with valid student details from Excel")
def submit_form_with_valid_student_details(context):
    student = read_student_from_excel()
    context.demoqa_form.submit_student_details(student)


@then("the form should be submitted successfully")
def form_should_be_submitted_successfully(context):
    expect(context.page.locator("#example-modal-sizes-title-lg")).to_have_text(
        "Thanks for submitting the form"
    )
