class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.add_to_cart_btn = ".inventory_item button"
        self.cart_icon = ".shopping_cart_link"

    def add_first_item_to_cart(self):
        self.page.click(self.add_to_cart_btn)

    def open_cart(self):
        self.page.click(self.cart_icon)
