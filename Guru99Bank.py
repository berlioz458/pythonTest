from selenium import webdriver

browser = webdriver.Chrome()

link = "http://www.demo.guru99.com/V4/"
browser.get(link)

userID = "mngr204244"
Password = "amadAnU"

userIdInput = browser.find_element_by_css_selector("[name = \"uid\"]")
userIdInput.send_keys(userID)

passwordInput = browser.find_element_by_css_selector("[name = \"password\"]")
passwordInput.send_keys(Password)

buttonLogin = browser.find_element_by_css_selector("[name=\"btnLogin\"]")
buttonLogin.click()
