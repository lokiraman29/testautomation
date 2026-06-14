Feature: DemoQA practice form

  @demoqaform
  Scenario: Submit practice form with valid student details
    Given I open the DemoQA practice form
    When I submit the form with valid student details from Excel
    Then the form should be submitted successfully
