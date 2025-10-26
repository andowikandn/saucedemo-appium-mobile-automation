from locators.sort import SortLocator
from locators.dashboard import DashboardLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class SortPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def sort_list(self):
        with allure.step('User sort list'):
            self.wait.until(
                EC.element_to_be_clickable(SortLocator.sort_list)).click()

    def get_sort_list(self):
        with allure.step('Get sort list'):
            assert self.wait.until(
                EC.presence_of_element_located(SortLocator.sort_list)).is_enabled()

    def sort_grid(self):
        with allure.step('User sort grid'):
            self.wait.until(
                EC.element_to_be_clickable(SortLocator.sort_grid)).click()

    def get_sort_grid(self):
        with allure.step('Get sort grid'):
            assert self.wait.until(
                EC.presence_of_element_located(SortLocator.sort_grid)).is_enabled()

    def tap_sort(self):
        with allure.step('User tap sort by'):
            self.wait.until(
                EC.element_to_be_clickable(SortLocator.tap_sort_by)).click()

    def get_sort_item(self):
        with allure.step('Get sort by items'):
            assert self.wait.until(
                EC.presence_of_element_located(SortLocator.sort_by_view)).is_displayed()

    def tap_sort_cancel(self):
        with allure.step('User tap cancel sort'):
            self.wait.until(
                EC.element_to_be_clickable(SortLocator.sort_by_cancel_btn)).click()

    def back_to_dashboard(self):
        with allure.step('Go back to dashboard'):
            assert self.wait.until(
                EC.presence_of_element_located(DashboardLocator.dashboard_page)).is_displayed()

    def sort_by_price_hilo(self):
        with allure.step('Sort by price high to low'):
            self.wait.until(
                EC.element_to_be_clickable(SortLocator.sort_by_price_hilo)).click()

    def get_by_price_hilo(self):
        with allure.step('Verify sort by price high to low'):
            assert self.wait.until(
                EC.presence_of_element_located(SortLocator.get_price_hilo_list)).is_displayed()

    def sort_by_price_lohi(self):
        with allure.step('Sort by price low to high'):
            self.wait.until(
                EC.element_to_be_clickable(SortLocator.sort_by_price_lohi)).click()

    def get_by_price_lohi(self):
        with allure.step('Verify sort by price low to high'):
            assert self.wait.until(
                EC.presence_of_element_located(SortLocator.get_price_lohi_list)).is_displayed()

    def sort_by_name_za(self):
        with allure.step('Sort by name Z to A'):
            self.wait.until(
                EC.element_to_be_clickable(SortLocator.sort_by_name_za)).click()

    def get_by_name_za(self):
        with allure.step('Verify sort by name Z to A'):
            assert self.wait.until(
                EC.presence_of_element_located(SortLocator.get_name_za_list)).is_displayed()

    def sort_by_name_az(self):
        with allure.step('Sort by name A to Z'):
            self.wait.until(
                EC.element_to_be_clickable(SortLocator.sort_by_name_az)).click()

    def get_by_name_az(self):
        with allure.step('Verify sort by name A to Z'):
            assert self.wait.until(
                EC.presence_of_element_located(SortLocator.get_name_az_list)).is_displayed()