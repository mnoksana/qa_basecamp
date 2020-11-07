from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

search_text = "selenium install ubuntu python"
driver = webdriver.Chrome('chromedriver')
wait = WebDriverWait(driver, 10)
driver.get("https://google.com/ncr")
driver.find_element_by_name("q").send_keys(search_text + Keys.RETURN)
wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
driver.find_element_by_partial_link_text('pypi').click()
driver.find_element_by_name("q").send_keys("selenium" + Keys.RETURN)
links = driver.find_elements_by_class_name("package-snippet")
links[1].click()
# driver.close()








