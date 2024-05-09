from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class ProfilePage(Form):
    def __init__(self):
        super().__init__(
            locator=Locator(By.XPATH, '//*[contains(text(), "Welcome")]'),
            name="Profile Page",
        )

    def get_name_user(self):
        profile_text = self._element_factory.get_text_box(
            locator=Locator(By.XPATH, '//*[contains(text(),"Welcome")] '),
            name='profile text',
        )
        return profile_text.text
