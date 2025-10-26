from locators.login import LoginLocator
from locators.dashboard import DashboardLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import allure

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def enter_username(self, username: str):
        with allure.step('Input username'):
            self.wait.until(
                EC.visibility_of_element_located(LoginLocator.username_field)).send_keys(username)
    
    def enter_password(self, password: str):
        with allure.step('Input password'):
            self.wait.until(
                EC.visibility_of_element_located(LoginLocator.password_field)).send_keys(password)
    
    def click_login(self):
        with allure.step('Tap login button'):
            self.wait.until(
                EC.element_to_be_clickable(LoginLocator.login_btn)).click()

    def tap_autofill_standard_user(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
            'new UiSelector().text("standard_user"))'
        ) # scroll down to tap
        sleep(0.5)
        with allure.step('Tap autofill standard user'):
            tap_auto = self.wait.until(
                EC.element_to_be_clickable(LoginLocator.auto_standard_user))
            tap_auto.click()
            assert tap_auto.is_displayed()

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollBackward().scrollIntoView(new UiSelector().text("LOGIN"))'
        ) # scroll up to login
        sleep(0.5)

    def verify_login_success(self):
        with allure.step('Verify login success'):
            dashboard_page = self.wait.until(
                EC.visibility_of_element_located(DashboardLocator.dashboard_page))
            assert dashboard_page.is_displayed()

    def verify_login_failed(self):
        with allure.step('Verify login error message'):
            handling_error = self.wait.until(
                EC.visibility_of_element_located(LoginLocator.error_msg))
            assert handling_error.is_displayed()
            return handling_error.text