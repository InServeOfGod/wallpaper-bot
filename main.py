import os

from selenium import webdriver

URL = "https://alphacoders.com/"
CWD = os.path.abspath(os.getcwd())
GECKODRIVER = os.path.join(CWD, 'geckodriver')


search_text = input(f"Search for in {URL} : ")

driver = webdriver.Firefox(executable_path=GECKODRIVER)
driver.get(URL)
driver.maximize_window()

search_box = driver.find_element(value='t')
search_box.click()
search_box.send_keys(search_text)
search_box.send_keys(webdriver.Keys.ENTER)
