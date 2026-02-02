from locators.checkout_locators import (
    FIRST_NAME_INPUT,
    LAST_NAME_INPUT,
    POSTAL_CODE_INPUT,
    CONTINUE_BUTTON,
    FINISH_BUTTON,
)


class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def fill_user_info(self, first, last, postal):
        self.page.fill(FIRST_NAME_INPUT, first)
        self.page.fill(LAST_NAME_INPUT, last)
        self.page.fill(POSTAL_CODE_INPUT, postal)
        self.page.click(CONTINUE_BUTTON)

    def finish_order(self):
        self.page.click(FINISH_BUTTON)
