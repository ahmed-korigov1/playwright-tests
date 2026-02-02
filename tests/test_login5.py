from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_full_buy_flow(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_item_to_cart()
    inventory_page.open_cart()

    cart_page.click_checkout()

    checkout_page.fill_user_info("John", "Doe", "12345")
    checkout_page.finish_order()

    assert "checkout-complete" in page.url
