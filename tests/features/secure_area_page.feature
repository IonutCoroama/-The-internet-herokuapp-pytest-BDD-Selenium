Feature: Test if the Secure Area page is displayed and secure
  As a user,
  I want to verify if the page is correctly displayed,
  and it works according to the specifications.


  Scenario: Test the page is displayed
    Given I successfully login
    Then the Secure Area page should open
    And a flash message should appear to confirm the successful login
    And the Title text should be visible and displaying the correct text
    And the Logout button should be displayed


  Scenario: Test if the logout from the Secure Area page is working
    Given I successfully login
    When I click Logout button
    Then the Login page should open
    And a flash message should appear to confirm the successful logout


  Scenario: Test if the logout from the Secure Area page is secure
    Given I successfully login
    And I click Logout button
    When I navigate backward using the Back button from the browser
    Then the browser should remain in the login page and should ask me to login again
