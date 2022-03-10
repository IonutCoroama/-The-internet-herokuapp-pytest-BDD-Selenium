from pytest_bdd import scenarios, parsers, given, when, then
from pages.home_internet_herokuapp_page import HomePage
from utils.generic_methods import GenericMethods
from utils.constants import Constants
import requests

scenarios('../features/home_page.feature')


@given(parsers.cfparse('I open the page "{page_url}"'))
def open_page(browser, page_url):
    generic = GenericMethods(browser)
    generic.load_page(page_url)


# @when('I launch the page')
# def do_nothing():
#     pass

@when('I scroll to the bottom of the page')
def scroll_to_bottom(browser):
    home_page = HomePage(browser)
    home_page.scroll_to_footer()


@when(parsers.cfparse('I click the "{link}"'))
def click_link(browser, link):
    home_page = HomePage(browser)
    home_page.click_link(link)


@then('the page should open')
def response_200():
    const = Constants
    response = requests.get(const.HOME_PAGE_URL)
    assert response.status_code == 200


@then('the Header text should be visible')
def is_header_visible(browser):
    home_page = HomePage(browser)
    assert home_page.is_heading_text_displayed(), 'Header is not displayed'


@then('the Title text should be visible')
def is_title_visible(browser):
    home_page = HomePage(browser)
    assert home_page.is_title_text_displayed(), 'Title is not displayed'


@then('the Header should contain the correct text')
def is_header_text_ok(browser):
    home_page = HomePage(browser)
    assert home_page.get_heading_text() == "Welcome to the-internet", "Heading text don\'t mach"


@then('the Title should contain the correct text')
def is_title_text_ok(browser):
    home_page = HomePage(browser)
    assert home_page.get_title_text() == 'Available Examples', "Title text don\'t mach"


@then('I should see the footer')
def is_footer_displayed(browser):
    home_page = HomePage(browser)
    assert home_page.is_footer_displayed(), 'Footer is not displayed'
    home_page.scroll_to_header()


@then('I should see some links displayed')
def is_some_links_displayed(browser):
    home_page = HomePage(browser)
    assert home_page.is_a_b_test_link_displayed(), 'A/B Testing link is not displayed'
    assert home_page.is_add_remove_elements_link_displayed(), 'Add/Remove Elements link is not displayed'
    assert home_page.is_broken_images_link_displayed(), 'Broken Images link is not displayed'
    assert home_page.is_form_authentication_link_displayed(), 'Form Authentication link is not displayed'


@then(parsers.cfparse('the "{page}" should open'))
def check_page(browser, page):
    # home_page = HomePage(browser)
    generic = GenericMethods(browser)
    assert generic.get_current_url() == page, 'link is not OK'


@then('the page should not contain broken images')
def check_for_broken_images(browser):
    generic = GenericMethods(browser)
    assert generic.is_broken_images_on_page(), 'The page contains broken images'
