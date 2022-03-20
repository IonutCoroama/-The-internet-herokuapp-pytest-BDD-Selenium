Feature: Test if the Add/Remove Elements page is functional
  As a user,
  I want to verify if the page is correctly displayed,
  and the buttons actions are as expected.


  Scenario: Test the page is displayed
    Given I open the page "https://the-internet.herokuapp.com/add_remove_elements/"
    Then the Title should contain the correct text
    And the Add Element button should be displayed


  Scenario: Test broken images
    Given I open the page "https://the-internet.herokuapp.com/add_remove_elements/"
    Then the page should not contain broken images


  Scenario: Test buttons works well
    Given I open the page "https://the-internet.herokuapp.com/add_remove_elements/"
    When I click the Add Element button "1" times
    Then I can see the Delete button appears
    And "1" Delete buttons should be displayed


  Scenario Outline: Test delete buttons number
    Given I open the page "https://the-internet.herokuapp.com/add_remove_elements/"
    When I click the Add Element button "<x>" times
    Then "<x>" Delete buttons should be displayed

  Examples: Number of buttons
    |x|
    |9|
    |30|
    |51|


  Scenario Outline: Test delete buttons number 2
    Given I open the page "https://the-internet.herokuapp.com/add_remove_elements/"
    When I click the Add Element button "<x>" times
    When I click the Delete button "<y>" times
    Then "<z>" Delete buttons should be displayed

  Examples: Number of buttons
    |x|y|z|
    |9|9|0  |
    |30|11|19|
    |51|41|10|