from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pytest


@pytest.fixture()
def setup_and_teardown():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    yield driver
    driver.quit()


def test_login_with_valid_credentials(setup_and_teardown):

    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys("aniketjai@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "input-password").send_keys("121212")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(1)
    assert driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()


def test_login_without_entering_credentials(setup_and_teardown):
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys("")
    time.sleep(1)
    driver.find_element(By.ID, "input-password").send_keys("")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(1)
    expected_warning = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warning)
