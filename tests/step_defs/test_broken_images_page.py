from pytest_bdd import scenarios, parsers, given, then
from pages.broken_images_page import BrokenImagesPage
from utils.generic_methods import GenericMethods


scenarios('../features/broken_images_page.feature')


@given(parsers.cfparse('I open the page "{page_url}"'))
def open_page(browser, page_url):
    generic = GenericMethods(browser)
    generic.load_page(page_url)


@then('the Title text should be visible')
def is_title_visible(browser):
    broken_images_page = BrokenImagesPage(browser)
    assert broken_images_page.is_title_text_visible()


@then('the Title should contain the correct text')
def is_title_text_correct(browser):
    broken_images_page = BrokenImagesPage(browser)
    assert broken_images_page.get_title_text() == "Broken Images", "The title is not displayed OK"


@then(parsers.cfparse('the "{image}" should be displayed'))
def is_image_displayed(browser, image):
    broken_images_page = BrokenImagesPage(browser)
    broken_images_page.is_image_visible(image)


@then('the page should not contain broken images')
def check_for_broken_images(browser):
    generic = GenericMethods(browser)
    assert generic.is_broken_images_on_page(), 'The page contains broken images'
