class LoginPage:
    #Locators
    USERNAME_FIELD = '[data-test="username"]'
    PASSWORD_FIELD = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    ERROR_MESSAGE = '[data-test="error"]'



    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):

        self.page.locator(self.USERNAME_FIELD).fill(username)
        self.page.locator(self.PASSWORD_FIELD).fill(password)
        self.page.locator(self.LOGIN_BUTTON).click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.page)

    def attempt_login(self, username, password):
        self.page.locator(self.USERNAME_FIELD).fill(username)
        self.page.locator(self.PASSWORD_FIELD).fill(password)
        self.page.locator(self.LOGIN_BUTTON).click()
        return self

    def get_error_message(self):
        return self.page.locator(self.ERROR_MESSAGE)
