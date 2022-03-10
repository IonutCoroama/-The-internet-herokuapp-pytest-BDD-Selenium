Feature: Test if the A/B Testing page is displayed
  As a user,
  I want to verify if the page is correctly displayed.

  Scenario: Test the page is displayed
    Given I open the page "https://the-internet.herokuapp.com/abtest"
    Then the page should open
    And the Title should contain the correct text


  Scenario: Test broken images
    Given I open the page "https://the-internet.herokuapp.com/abtest"
    Then the page should not contain broken images