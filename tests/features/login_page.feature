Feature: Test if the Form Authentication page is displayed
  As a user,
  I want to verify if the page is correctly displayed,
  and it works according to the specifications.


  Scenario: Test the page is displayed
    Given I open the page "https://the-internet.herokuapp.com/login"
    Then the Title should contain the correct text
    And the username field should appear
    And the password field should appear
    And the Login button should be displayed


  Scenario: Login using valid credentials
    Given I open the page "https://the-internet.herokuapp.com/login"
    And I type the username "tomsmith"
    And I type the password "SuperSecretPassword!"
    When I click the Login button
    Then the secure page should open
    And a flash message should appear to confirm the successful login


  Scenario Outline: Login using invalid credentials
    Given I open the page "https://the-internet.herokuapp.com/login"
    And I type the username "<user>"
    And I type the password "<password>"
    When I click the Login button
    Then the secure page should not open
    And a warning "<message>" should appear

    Examples: Invalid credentials
    |user|password|message|
    |tomsmith1|SuperSecretPassword!|Your username is invalid!|
    |TOMSMITH|SuperSecretPassword!|Your username is invalid!|
    |tomsmith|SuperPassword!|Your password is invalid!|
    |tomasmith|SuperMegaPassword!|Your username is invalid!|
    |asdsef|safff123!|Your username is invalid!|


  Scenario: Try to login with random credentials
    Given I open the page "https://the-internet.herokuapp.com/login"
    And I type a random username
    And I type a random password
    When I click the Login button
    Then the secure page should not open
    And a warning "Your username is invalid!" should appear