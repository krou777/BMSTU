from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://ya.ru")


search_input = driver.find_element(By.XPATH, "//input[@class='search3__input mini-suggest__input']")
search_input.send_keys("Hello world")

search_button = driver.find_element(By.XPATH, "//button[contains(text(),'Найти')]")
search_button.click()

s = driver.current_url
print(s)
