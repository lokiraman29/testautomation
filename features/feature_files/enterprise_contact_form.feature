Feature: Optus Enterprise contact form
  As an Enterprise visitor
  I want to submit my contact details
  So that Optus can contact me about its services

  Scenario: Submit the Enterprise contact form
    Given I have loaded the Optus Enterprise contact form
    When I submit the Enterprise contact form using the "valid_contact" test data
    Then the Enterprise contact form should be submitted successfully
