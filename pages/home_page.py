from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class HomePage(Form):
    def __init__(self):
        super().__init__(
            locator=Locator(By.XPATH, '//*[contains(text(),"Test home page")]'),
            name='Home Page',
        )
