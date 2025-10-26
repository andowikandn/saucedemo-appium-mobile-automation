from appium.webdriver.common.appiumby import AppiumBy

class ViewProductLocator:
    your_cart_page = (AppiumBy.XPATH, '//android.widget.TextView[@text="YOUR CART"]')
    view_product_backpack_on_img = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Image Container"]/android.widget.ImageView')
    view_product_backpack_on_txt = (AppiumBy.XPATH, '//android.widget.TextView[@text="Sauce Labs Backpack"]')
    add_cart_backpack_in_detail = (AppiumBy.ACCESSIBILITY_ID, 'test-ADD TO CART')
    view_add_cart_badge = (AppiumBy.XPATH, '//android.widget.TextView[@text="1"]')
    remove_cart_badge = (AppiumBy.ACCESSIBILITY_ID, 'test-REMOVE')
    view_remove_cart_badge = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]/android.view.ViewGroup')
    back_to_product_btn = (AppiumBy.ACCESSIBILITY_ID, 'test-BACK TO PRODUCTS')
    continue_shopping_btn = (AppiumBy.ACCESSIBILITY_ID, 'test-CONTINUE SHOPPING')
    checkout_btn = (AppiumBy.ACCESSIBILITY_ID, 'test-CHECKOUT')