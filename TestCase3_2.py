import unittest
from selenium import webdriver
import time


class MyTestClass(unittest.TestCase):
    def test_first(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element_by_css_selector("div.first_block .first")
        first_name.send_keys("Kate")
        second_name = browser.find_element_by_css_selector("div.first_block .second")
        second_name.send_keys("Pavlova")
        e_mail = browser.find_element_by_css_selector("div.first_block .third")
        e_mail.send_keys("eMail@mail.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
        #self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text, "Bad request")

    def test_second(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector("div.first_block .first")
        first_name.send_keys("Kate")
        second_name = browser.find_element_by_css_selector("div.first_block .second")
        second_name.send_keys("Pavlova")
        e_mail = browser.find_element_by_css_selector("div.first_block .third")
        e_mail.send_keys("eMail@mail.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
        # self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text, "Bad request")


if __name__ == "__main__":
    unittest.main()
