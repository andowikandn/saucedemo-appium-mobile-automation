from appium.webdriver.common.appiumby import AppiumBy

class LoginLocator:
    username_field = (AppiumBy.ACCESSIBILITY_ID, 'test-Username')
    password_field = (AppiumBy.ACCESSIBILITY_ID, 'test-Password')
    login_btn = (AppiumBy.XPATH, '//android.widget.TextView[@text="LOGIN"]')
    error_msg = (AppiumBy.CLASS_NAME, 'android.widget.TextView')
    login_page = (AppiumBy.XPATH, '//android.widget.ScrollView[@content-desc="test-Login"]')
    auto_standard_user = (AppiumBy.XPATH, '//android.widget.TextView[@text="standard_user"]')