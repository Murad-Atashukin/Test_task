from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class RegistrationPage(Form):
    def __init__(self):
        super().__init__(
            locator=Locator(By.NAME, "name"),
            name='Registration Page',
        )

    def set_email(self, email):
        email_field = self._element_factory.get_text_box(
            locator=Locator(By.NAME, "email"),
            name='email field',
        )
        email_field.type(email)

    def set_name(self, name):
        name_field = self._element_factory.get_text_box(
            locator=Locator(By.NAME, "name"),
            name='name field',
        )
        name_field.type(name)

    def set_password(self, password):
        password_field = self._element_factory.get_text_box(
            locator=Locator(By.NAME, "password"),
            name='password field',
        )
        password_field.type(password)

    def click_button_sign_up(self):
        button_sign_up = self._element_factory.get_button(
            locator=Locator(By.XPATH, '//*[contains(@class, "button")]'),
            name='button sign up',
        )
        button_sign_up.click()
