import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_search_for_a_valid_product():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    driver.find_element(By.NAME,"search").send_keys("HP")
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    time.sleep(2)
    driver.quit()