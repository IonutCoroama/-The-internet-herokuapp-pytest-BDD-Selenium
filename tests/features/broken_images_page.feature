Feature: Test if the Broken Images page is opening and contains broken images
  As a user,
  I want to verify if the page is correctly displayed,
  and contains broken images.


  Scenario: Test the page is displayed
    Given I open the page "https://the-internet.herokuapp.com/broken_images"
    Then the Title text should be visible
    And the Title should contain the correct text


  Scenario: Test broken images
    Given I open the page "https://the-internet.herokuapp.com/broken_images"
    Then the page should not contain broken images


  Scenario Outline: Test images are displayed
    Given I open the page "https://the-internet.herokuapp.com/broken_images"
    Then the "<image>" should be displayed

  Examples: List of images
    |image|
    |2|
    |3|
    |4|