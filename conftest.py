from appium import webdriver
import pytest
from appium.options.android.uiautomator2.base import UiAutomator2Options

@pytest.fixture
def driver():
    options = UiAutomator2Options()

    options.udid = 'emulator-5554' # Emulator => Google Pixel M1
    options.platform_name = 'Android'
    options.app_package = 'com.swaglabsmobileapp'
    options.app_activity = 'com.swaglabsmobileapp.MainActivity'
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

    yield driver 
    driver.quit()