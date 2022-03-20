from pytest_bdd import scenarios, parsers, given, when, then
from pages.add_remove_elements_page import AddRemoveElementsPage
from utils.generic_methods import GenericMethods


scenarios('../features/add_remove-elements_page.feature')


@given(parsers.cfparse('I open the page "{page_url}"'))
def open_page(browser, page_url):
    generic = GenericMethods(browser)
    generic.load_page(page_url)


@when(parsers.cfparse('I click the Add Element button "{x}" times'))
def click_add_element_button(browser, x):
    add_remove_elements_page = AddRemoveElementsPage(browser)
    x = int(x)
    for i in range(x):
        add_remove_elements_page.click_add_element_button()


@when(parsers.cfparse('I click the Delete button "{y}" times'))
def click_delete_button(browser, y):
    add_remove_elements_page = AddRemoveElementsPage(browser)
    y = int(y)
    for i in range(1, y + 1):
        add_remove_elements_page.click_delete_button()


@then('the Title should contain the correct text')
def is_title_text_ok(browser):
    add_remove_elements_page = AddRemoveElementsPage(browser)
    assert add_remove_elements_page.get_title_text() == "Add/Remove Elements", "Title is not OK"


@then('the Add Element button should be displayed')
def is_add_element_button_displayed(browser):
    add_remove_elements_page = AddRemoveElementsPage(browser)
    assert add_remove_elements_page.is_add_element_button_displayed(), "Add/Remove Elements button is not displayed"


@then('the page should not contain broken images')
def check_for_broken_images(browser):
    generic = GenericMethods(browser)
    assert generic.is_broken_images_on_page(), 'The page contains broken images'


@then('I can see the Delete button appears')
def delete_button_is_displayed(browser):
    add_remove_elements_page = AddRemoveElementsPage(browser)
    assert add_remove_elements_page.is_delete_element_button_displayed(), "Delete button is not displayed"


@then(parsers.cfparse('"{x}" Delete buttons should be displayed'))
def number_of_delete_buttons(browser, x):
    add_remove_elements_page = AddRemoveElementsPage(browser)
    x = int(x)
    assert add_remove_elements_page.get_number_of_delete_buttons() == x, "Delete button number is not ok"
