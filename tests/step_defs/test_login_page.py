from pytest_bdd import scenarios, parsers, given, when, then
from pages.form_authentication_page import LoginPage
from utils.generic_methods import GenericMethods
from utils.constants import Constants

const = Constants
scenarios('../features/login_page.feature')


@given(parsers.cfparse('I open the page "{page_url}"'))
def open_page(browser, page_url):
    generic = GenericMethods(browser)
    generic.load_page(page_url)


@given(parsers.cfparse('I type the username "{valid_username}"'))
def type_username(browser, valid_username):
    login_page = LoginPage(browser)
    login_page.type_username(valid_username)


@given(parsers.cfparse('I type the password "{valid_password}"'))
def type_password(browser, valid_password):
    login_page = LoginPage(browser)
    login_page.type_password(valid_password)


@given('I type a random username')
def type_random_user(browser):
    generic = GenericMethods(browser)
    login_page = LoginPage(browser)
    random_username = generic.generate_username()
    login_page.type_username(random_username)


@given('I type a random password')
def type_random_password(browser):
    generic = GenericMethods(browser)
    login_page = LoginPage(browser)
    random_password = generic.generate_username()
    login_page.type_password(random_password)


@when('I click the Login button')
def click_login_button(browser):
    login_page = LoginPage(browser)
    login_page.click_login_button()


@then('the Title should contain the correct text')
def is_title_text_correct(browser):
    login_page = LoginPage(browser)
    assert login_page.get_title_text() == "Login Page", 'Page title is not OK'


@then('the username field should appear')
def is_user_field_displayed(browser):
    login_page = LoginPage(browser)
    assert login_page.is_username_field_displayed(), 'Username field is not displayed'


@then('the password field should appear')
def is_password_field_displayed(browser):
    login_page = LoginPage(browser)
    assert login_page.is_password_field_displayed(), 'Password field is not displayed'


@then('the Login button should be displayed')
def is_password_field_displayed(browser):
    login_page = LoginPage(browser)
    assert login_page.is_login_button_displayed(), 'Login button is not displayed'


@then('the secure page should open')
def is_secure_area_page_displayed(browser):
    generic = GenericMethods(browser)
    assert generic.get_current_url() == const.SECURE_AREA_URL, 'Login not successful: Secure area page is not opening'


@then('the secure page should not open')
def is_secure_area_page_not_displayed(browser):
    generic = GenericMethods(browser)
    assert generic.get_current_url() == const.FORM_AUTHENTICATION_URL, 'Unexpected redirect from login page'


@then('a flash message should appear to confirm the successful login')
def is_flash_message_displayed(browser):
    login_page = LoginPage(browser)
    assert login_page.is_login_successful_message_displayed(), "Successful login message not OK"


@then(parsers.cfparse('a warning "{message}" should appear'))
def is_flash_message_ok(browser, message):
    generic = GenericMethods(browser)
    assert message in generic.get_flash_message(), 'Flash message is not ok'
