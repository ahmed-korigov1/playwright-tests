class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, text):
        self.page.fill(locator, text)

    def go_to(self, url):
        self.page.goto(url)
