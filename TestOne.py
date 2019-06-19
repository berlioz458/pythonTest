import time

from selenium import webdriver

browser = webdriver.Chrome()
link = "https://www.ozon.ru"
browser.get(link)
time.sleep(5)

# search input
test_css_selector = "[data-test-id=\"header-search-input\"]"
search_pool = browser.find_element_by_css_selector(test_css_selector)
search_pool.send_keys("1212")

# search button
search_button = browser.find_element_by_css_selector("[data-test-id=\"header-search-go\"]")
search_button.click()
time.sleep(3)

# add carts
i = 0
while i < 2:
    carts_xpath = "//div[@data-index=\"" + str(i) + "\"]/div/div/button[@data-test-id=\"tile-buy-button\"]"
    add_cart = browser.find_element_by_xpath(carts_xpath)
    browser.execute_script("return arguments[0].scrollIntoView(true);", add_cart)
    add_cart.click()
    i = i + 1

shop_basket = browser.find_element_by_css_selector("a[href=\"/context/cart\"]")
browser.execute_script("return arguments[0].scrollIntoView(true);", shop_basket)
shop_basket.click()
time.sleep(3)

delete_buttons = browser.find_elements_by_css_selector("[data-test-id=\"cart-item-delete-btn\"]")
for del_but in delete_buttons:
    print(del_but)
    del_but.click()
    del_but2 = browser.find_element_by_css_selector("[data-test-id=\"checkcart-confirm-modal-confirm-button\"]")
    del_but2.click()
    time.sleep(1)

