from appium.webdriver.common.appiumby import AppiumBy

class DashboardLocator:
    # dashboard product page
    logo_dashboard = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-header"]//android.widget.ImageView[2]')
    dashboard_page = (AppiumBy.XPATH, '//android.widget.TextView[@text="PRODUCTS"]')
    
    # product items action
    tap_product_img_backpack = (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-Item"])[1]/android.view.ViewGroup/android.widget.ImageView')
    tap_product_txt_backpack = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="test-Item title" and @text="Sauce Labs Backpack"]')
    add_to_cart_backpack_in_dashboard = (AppiumBy.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[1]')
    add_to_cart_jacket = (AppiumBy.XPATH, '(//android.widget.TextView[@text="ADD TO CART"])[2]') # scroll down first to tap
    cart_badge = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]')
    view_add_carts_badge = (AppiumBy.XPATH, '//android.widget.TextView[@text="2"]')
    remove_cart_backpack = (AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-REMOVE"])[1]')
    view_remove_cart_badge = (AppiumBy.XPATH, '//android.widget.TextView[@text="1"]')
    tap_sidebar = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Menu"]')
    scroll_to_privacy = (AppiumBy.XPATH, '//android.widget.TextView[@text="Terms of Service | Privacy Policy"]')