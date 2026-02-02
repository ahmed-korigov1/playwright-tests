from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_buy_flow(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_item_to_cart()
    inventory_page.open_cart()

    assert "cart" in page.url
