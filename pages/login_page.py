from pages.base_page import BasePage
from locators.login_locators import (
    USERNAME_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
)


class LoginPage(BasePage):

    def open(self):
        self.go_to(self.page.base_url)

    def login(self, user, password):
        self.fill(USERNAME_INPUT, user)
        self.fill(PASSWORD_INPUT, password)
        self.click(LOGIN_BUTTON)
