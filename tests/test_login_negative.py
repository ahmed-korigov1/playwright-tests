from pages.login_page import LoginPage


def test_login_invalid_user(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    assert "Epic sadface" in page.content()
