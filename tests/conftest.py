import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    options = Options()
    # this parameter tells Chrome that
    # it should be run without UI (Headless)
    options.headless = False
    # initializing webdriver for Chrome with our options
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()
