Feature: Optus Enterprise mega navigation
  As an Optus Enterprise visitor
  I want to open each main navigation category
  So that I can explore the available enterprise content

  Background:
    Given I am on the Optus Enterprise page

  Scenario: Open every Enterprise mega-navigation category on the same page
    When I open the Enterprise mega-navigation categories from the "all_categories" test data
    Then every requested mega-navigation panel should be visible
