import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture
def setup_and_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_search_for_a_valid_product(setup_and_teardown):
    driver = setup_and_teardown
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    assert driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    time.sleep(2)


def test_search_for_an_invalid_product(setup_and_teardown):
    driver = setup_and_teardown
    driver.find_element(By.NAME, "search").send_keys("Honda")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//input[@id='button-search']//following-sibling::p").text == expected_text
    time.sleep(2)


def test_search_without_providing_any_product(setup_and_teardown):
    driver = setup_and_teardown
    driver.find_element(By.NAME, "search").send_keys("")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//input[@id='button-search']//following-sibling::p").text == expected_text
    time.sleep(2)
