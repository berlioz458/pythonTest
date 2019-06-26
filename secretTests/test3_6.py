import pytest
import time
import math
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test..")
    browser = webdriver.Chrome()
    # добавление ожидание прогрузки браузера
    browser.implicitly_wait(20)
    yield browser
    print("\nQuit browser..")
    browser.quit()

# пишет параметр и далее варианты для него
@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lesson):
    link = "https://stepik.org/lesson/{}/step/1".format(lesson)
    browser.get(link)
    # time.sleep(5)
    input_answer = browser.find_element_by_css_selector("textarea.ember-view")
    answer = math.log(int(time.time()))
    input_answer.send_keys(str(answer))
    btn = browser.find_element_by_css_selector("button.submit-submission")
    # time.sleep(2)
    btn.click()
    # time.sleep(3)
    text_box = browser.find_element_by_css_selector("pre.smart-hints__hint")
    text_pass = text_box.text

    assert text_pass == "Correct!", "Bad request"
