import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
])
def test_login_different_users(page, username, password):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username, password)

    assert "inventory" in page.url
