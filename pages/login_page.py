from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class LoginPage(Form):
    def __init__(self):
        super().__init__(
            locator=Locator(By.XPATH, '//*[text()="Login"]'),
            name='Login Page',
        )

    def set_email(self, email):
        email_field = self._element_factory.get_text_box(
            locator=Locator(By.NAME, "email"),
            name='email field',
        )
        email_field.type(email)

    def set_password(self, password):
        password_field = self._element_factory.get_text_box(
            locator=Locator(By.NAME, "password"),
            name='password field',
        )
        password_field.type(password)

    def click_button_login(self):
        button_login = self._element_factory.get_button(
            locator=Locator(By.XPATH, '//*[contains(@class, "button")]'),
            name='button login',
        )
        button_login.click()
