from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def generate_email_timestamp(self):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        timestamp = timestamp.replace('-', '_').replace(' ', '_').replace(':', '_')
        return "aniket" + timestamp + "@gmail.com"

    def test_create_account_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Aniket")
        time.sleep(1)
        self.driver.find_element(By.ID, "input-lastname").send_keys("Jaiswal")
        time.sleep(1)
        # once to run the script ,you will need to update the email as you can not register with already registered email.
        # here we use email with timestamp
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_timestamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("1245365478")
        self.driver.find_element(By.ID, "input-password").send_keys("121212")
        self.driver.find_element(By.ID, "input-confirm").send_keys("121212")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(1)
        expected_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)

    def test_login_with_all_required_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Aniket")
        time.sleep(1)
        self.driver.find_element(By.ID, "input-lastname").send_keys("Jaiswal")
        time.sleep(1)
        # once to run the script ,you will need to update the email as you can not register with already registered email.
        # here we use email with timestamp
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_timestamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("1245365478")
        self.driver.find_element(By.ID, "input-password").send_keys("121212")
        self.driver.find_element(By.ID, "input-confirm").send_keys("121212")
        self.driver.find_element(By.XPATH, "//input[@value='1'][@name='newsletter']").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(1)
        expected_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)
