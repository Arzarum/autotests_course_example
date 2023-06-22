from atf.ui import *


class AuthPage(Region):
    login_input = TextField(By.CSS_SELECTOR, "[name='Login']", 'Логин')
    password_input = TextField(By.CSS_SELECTOR, "[name='Password']", 'Пароль')

    def auth(self, login_input: str, password_input: str, url: str):
        """Авторизация"""

        self.browser.open(url)
        self.login_input.send_keys(login_input + Keys.ENTER)
        self.login_input.should_be(ExactText(login_input))
        self.password_input.type_in(password_input + Keys.ENTER)
