from appium.webdriver.common.appiumby import AppiumBy

class SidebarMenuLocator:
    burger_menu = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Menu"]')
    close_burger = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Close"]')
    all_items = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart drop zone"]')
    webview_menu = (AppiumBy.XPATH, '//android.widget.TextView[@text="WEBVIEW"]')
    webview_input_url = (AppiumBy.ACCESSIBILITY_ID, 'test-enter a https url here...')
    webview_goto_site = (AppiumBy.ACCESSIBILITY_ID, 'test-GO TO SITE')
    logo_bing = (AppiumBy.XPATH, '//android.widget.Image[@resource-id="bLogo"]') # Text: Microsoft Logo Image
    logout_menu = (AppiumBy.XPATH, '//android.widget.TextView[@text="LOGOUT"]')