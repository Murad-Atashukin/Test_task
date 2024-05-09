from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class PagesMenu(Form):
    def __init__(self):
        super().__init__(
            locator=Locator(By.CLASS_NAME, "navbar-end"),
            name='Pages menu',
        )

    def go_to_login_page(self):
        button_login = self._element_factory.get_button(
            locator=Locator(By.XPATH, '//*[@href="/login"]'),
            name='button login',
        )
        button_login.click()

    def go_to_registration_page(self):
        button_registration = self._element_factory.get_button(
            locator=Locator(By.XPATH, '//*[@href="/signup"]'),
            name='button login',
        )
        button_registration.click()
