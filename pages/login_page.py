from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email = page.get_by_role("textbox", name="Your Email")
        self.password = page.get_by_role("textbox", name="Your Password")
        self.login_btn = page.get_by_role("button", name="Login")
        self.alert_message = self.page.locator("//div[contains(text(),'Email hoặc mật khẩu không đúng !')]")

    def enter_email(self, mail):
        self.email.fill(mail)

    def enter_password(self, password):
        self.password.fill(password)

    @property
    def login_button(self):
        return self.login_btn

    def click_login(self):
        self.login_btn.click()

    def do_login(self, credentials):
        self.enter_email(credentials['email'])
        self.enter_password(credentials['password'])
        self.click_login()

    @property
    def err_msg_loc(self):
        return self.alert_messsage