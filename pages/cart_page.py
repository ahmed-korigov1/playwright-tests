from locators.cart_locators import CHECKOUT_BUTTON


class CartPage:

    def __init__(self, page):
        self.page = page

    def click_checkout(self):
        self.page.click(CHECKOUT_BUTTON)
