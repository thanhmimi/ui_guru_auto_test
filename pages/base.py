from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage(object):
    DEFAULT_TIMEOUT = 30

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visible(self, by, locator):
        """Wait for an element visible"""
        driver = self.driver
        return WebDriverWait(driver, self.DEFAULT_TIMEOUT).until(
            expected_conditions.visibility_of_element_located((by, locator)))

    def wait_for_elements_visible(self, by, locator):
        """Wait for elements visible"""
        driver = self.driver
        WebDriverWait(driver, self.DEFAULT_TIMEOUT).until(
            expected_conditions.visibility_of_all_elements_located((by, locator)))
        return driver.find_elements(by, locator)

    def wait_for_element_not_visible(self, by, locator):
        """Wait for an element invisible"""
        driver = self.driver
        return WebDriverWait(driver, self.DEFAULT_TIMEOUT).until(
            expected_conditions.invisibility_of_element_located((by, locator)))

    def have_element_displayed(self, by, locator):
        driver = self.driver
        try:
            WebDriverWait(driver, timeout=6).until(expected_conditions.visibility_of_element_located((by, locator)))
        except TimeoutException:
            return False
        return True
