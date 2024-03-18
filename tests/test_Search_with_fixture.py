import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("HP")
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
        time.sleep(2)

    def test_search_for_an_invalid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//input[@id='button-search']//following-sibling::p").text.__eq__(expected_text)
        time.sleep(2)

    def test_search_without_providing_any_product(self, ):
        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//input[@id='button-search']//following-sibling::p").text.__eq__(expected_text)
        allure.attach(self.driver.get_screenshot_as_png(),name="search_without_providing_any_product",attachment_type=AttachmentType.PNG)
        time.sleep(2)
