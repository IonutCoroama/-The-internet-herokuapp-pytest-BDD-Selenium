from pytest_bdd import scenarios, given, when, then
from pages.secure_area_page import SecureAreaPage
from utils.generic_methods import GenericMethods
from utils.constants import Constants


const = Constants
scenarios('../features/secure_area_page.feature')


@given('I successfully login')
def login_with_valid_credentials(browser):
    generic = GenericMethods(browser)
    generic.login_valid_account()


@given('I click Logout button')
def click_logout_button(browser):
    secure_page = SecureAreaPage(browser)
    secure_page.click_logout_button()


@when('I click Logout button')
def click_logout_button(browser):
    secure_page = SecureAreaPage(browser)
    secure_page.click_logout_button()


@when('I navigate backward using the Back button from the browser')
def go_to_previous_page(browser):
    browser.back()


@then('the Secure Area page should open')
def is_secure_area_page_displayed(browser):
    generic = GenericMethods(browser)
    assert generic.get_current_url() == const.SECURE_AREA_URL, 'We are not in the secure area'


@then('a flash message should appear to confirm the successful login')
def is_flash_login_message_ok(browser):
    generic = GenericMethods(browser)
    assert const.SUCCESS_LOGIN_MESSAGE in generic.get_flash_message(), 'Flash message successful login not ok'


@then('the Title text should be visible and displaying the correct text')
def is_title_text_ok(browser):
    secure_page = SecureAreaPage(browser)
    assert secure_page.get_title_text() == 'Secure Area', 'Title text is not OK'


@then('the Logout button should be displayed')
def is_logout_button_displayed(browser):
    secure_page = SecureAreaPage(browser)
    assert secure_page.is_logout_button_displayed(), 'Logout button is not displayed'


@then('the Login page should open')
def is_login_page_openned(browser):
    generic = GenericMethods(browser)
    assert generic.get_current_url() == const.FORM_AUTHENTICATION_URL


@then('a flash message should appear to confirm the successful logout')
def is_flash_logout_message_ok(browser):
    generic = GenericMethods(browser)
    assert const.SUCCESS_LOGOUT_MESSGE in generic.get_flash_message(), 'Flash message successful logout not ok'


@then('the browser should remain in the login page and should ask me to login again')
def is_current_url_ok(browser):
    generic = GenericMethods(browser)
    assert generic.get_current_url() is const.FORM_AUTHENTICATION_URL, \
        'Unsecure logout: If we go back after logout, we are logged in back'
