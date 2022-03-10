from pytest_bdd import scenarios, parsers, given, when, then
from pages.ab_test_page import AbTestingPage
from utils.generic_methods import GenericMethods
from utils.constants import Constants
import requests

scenarios('../features/ab_test_page.feature')


@given(parsers.cfparse('I open the page "{page_url}"'))
def open_page(browser, page_url):
    generic = GenericMethods(browser)
    generic.load_page(page_url)


@then('the page should open')
def response_200():
    const = Constants
    response = requests.get(const.AB_TEST_URL)
    assert response.status_code == 200


@then('the Title should contain the correct text')
def is_title_text_ok(browser):
    a_b_testing_page = AbTestingPage(browser)
    assert "A/B Test" in a_b_testing_page.get_title_text(), "AB test page is not displayed OK"


@then('the page should not contain broken images')
def check_for_broken_images(browser):
    generic = GenericMethods(browser)
    assert generic.is_broken_images_on_page(), 'The page contains broken images'
