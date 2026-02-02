from locators.login_locators import (
    USERNAME_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
)


class LoginPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.page.base_url)

    def login(self, user, password):
        self.page.fill(USERNAME_INPUT, user)
        self.page.fill(PASSWORD_INPUT, password)
        self.page.click(LOGIN_BUTTON)
