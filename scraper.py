from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://shopee.tw/mall/%E6%9B%B8%E7%B1%8D%E5%8F%8A%E9%9B%9C%E8%AA%8C%E6%9C%9F%E5%88%8A-cat.11041120')
time.sleep(5)

cards = driver.find_elements(By.CSS_SELECTOR, "div[class='a5oo3a kipA12']")

items = []
for card in cards:
    name = card.find_element(By.CLASS_NAME, "div[class='_4Ptt6k PF5Dnk GUhIR5']").text
    price = card.find_element(By.CLASS_NAME, "div[class='vfMKdL khnKnK']").text
    link = card.find_element(By.TAG_NAME, "a").get_attribute('herf')


    items.append((name, price, link))

print(items)
driver.quit()