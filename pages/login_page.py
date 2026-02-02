class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    def open(self):
        self.page.goto(self.page.base_url)

    def login(self, user, password):
        self.page.fill(self.username_input, user)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)