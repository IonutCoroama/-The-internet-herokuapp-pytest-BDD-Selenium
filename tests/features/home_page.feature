Feature: Test if the the-internet.herokuapp.com page is displayed
  As a user,
  I want to verify if the page is correctly displayed,
  and if the links are working and the page contains broken images.


  Scenario: Test the page is displayed
    Given I open the page "https://the-internet.herokuapp.com/"
#    When I launch the page
    Then the page should open
    And the Header text should be visible
    And the Title text should be visible
    And the Header should contain the correct text
    And the Title should contain the correct text


  Scenario: Test footer is displayed
    Given I open the page "https://the-internet.herokuapp.com/"
    When I scroll to the bottom of the page
    Then I should see the footer


  Scenario: Test links displayed
    Given I open the page "https://the-internet.herokuapp.com/"
    Then I should see some links displayed


  Scenario Outline: Test links are working
    Given I open the page "https://the-internet.herokuapp.com/"
    When I click the "<link>"
    Then the "<page>" should open

    Examples: Links
    |   link    |   page    |
    |ab_test_link|https://the-internet.herokuapp.com/abtest|
    |add_remove_elements_link|https://the-internet.herokuapp.com/add_remove_elements/|
    |broken_images_link|https://the-internet.herokuapp.com/broken_images|
    |form_authentication_link|https://the-internet.herokuapp.com/login|


  Scenario: Test broken images
    Given I open the page "https://the-internet.herokuapp.com/"
    Then the page should not contain broken images

