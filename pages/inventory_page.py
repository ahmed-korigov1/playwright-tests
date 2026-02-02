from locators.inventory_locators import (
    ADD_TO_CART_BUTTON,
    CART_LINK,
)


class InventoryPage:

    def __init__(self, page):
        self.page = page

    def add_first_item_to_cart(self):
        self.page.click(ADD_TO_CART_BUTTON)

    def open_cart(self):
        self.page.click(CART_LINK)
