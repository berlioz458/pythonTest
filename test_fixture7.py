import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# пишет параметр и далее варианты для него
@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = "http://selenium1py.pythonanywhere.com/{}/".format(language)
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
