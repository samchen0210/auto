from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://shopee.tw/mall/%E6%9B%B8%E7%B1%8D%E5%8F%8A%E9%9B%9C%E8%AA%8C%E6%9C%9F%E5%88%8A-cat.11041120')

ActionChains(driver).move_by_offset(100, 100).click().perform()

locator = (By.CSS_SELECTOR, "div[class='a5oo3a kipA12']")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(locator),
    '找不到指定商品'
)

cards = driver.find_elements(By.CSS_SELECTOR, "div[class='a5oo3a kipA12']")

items = []
for card in cards:
    try:
        ActionChains(driver).move_to_element(card).perform()
        name = card.find_element(By.CSS_SELECTOR, "div[class='_4Ptt6k PF5Dnk GUhIR5']").text
        price = card.find_element(By.CSS_SELECTOR, "div[class='R3a6HL LhSLR-']").text
        link = card.find_element(By.TAG_NAME, "a").get_attribute('href')
        
        items.append((name, price, link))
    except:
        break


print(items)
driver.quit()