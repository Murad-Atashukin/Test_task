import pytest

from pages.forms.pages_menu import PagesMenu
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.registration_page import RegistrationPage
from py_selenium_auto_core.logging.logger import Logger
from utils.string_utils import StringUtils


class TestHomePage:
    def test_registration_user(self):
        Logger.info("Test case 'test_registration_user' launched")
        Logger.info("Go to home page")
        home_page = HomePage()
        assert home_page.state.is_displayed(), "Home page is not open"

        Logger.info("Go to registration page")
        pages_menu = PagesMenu()
        pages_menu.go_to_registration_page()
        registration_page = RegistrationPage()
        assert registration_page.state.is_displayed(), "Registration page is not open."

        Logger.info("Registration user")
        Logger.info("Set email")
        global email_first_user
        email_first_user = StringUtils.generate_random_email()
        registration_page.set_email(email=email_first_user)
        Logger.info("Set name")
        global name_first_user
        name_first_user = StringUtils.generate_random_string()
        registration_page.set_name(name=name_first_user)
        Logger.info("Set password")
        global password_first_user
        password_first_user = StringUtils.generate_random_string()
        registration_page.set_password(password=password_first_user)

        Logger.info("Go to login page")
        registration_page.click_button_sign_up()
        login_page = LoginPage()
        assert login_page.state.is_displayed(), "Login page is not open. Incorrect registration"
        Logger.info("Test case 'test_registration_user' completed successfully")

    def test_login_user(self):
        Logger.info("Test case 'test_login_user' launched")
        Logger.info("Go to home page")
        home_page = HomePage()
        assert home_page.state.is_displayed(), "Home page is not open"

        Logger.info("Go to login page")
        pages_menu = PagesMenu()
        pages_menu.go_to_login_page()
        login_page = LoginPage()
        assert login_page.state.is_displayed(), "Login page is not open."

        Logger.info("Login user")
        Logger.info("Set email")
        login_page.set_email(email=email_first_user)
        Logger.info("Set password")
        login_page.set_password(password=password_first_user)

        Logger.info("Go to profile page")
        login_page.click_button_login()
        profile_page = ProfilePage()
        assert profile_page.state.is_displayed(), "Profile page is not open. Incorrect login"

        Logger.info("Checking user name")
        profile_text = profile_page.get_name_user()
        assert name_first_user in profile_text, "User name is false"
        Logger.info("Test case 'test_login_user' completed successfully")

    @pytest.mark.xfail
    def test_registration_user_without_password(self):
        Logger.info("Test case 'test_registration_user_without_password' launched")
        Logger.info("Go to home page")
        home_page = HomePage()
        assert home_page.state.is_displayed(), "Home page is not open"

        Logger.info("Go to registration page")
        pages_menu = PagesMenu()
        pages_menu.go_to_registration_page()
        registration_page = RegistrationPage()
        assert registration_page.state.is_displayed(), "Registration page is not open."

        Logger.info("Registration user without password")
        Logger.info("Set email")
        email_second_user = StringUtils.generate_random_email()
        registration_page.set_email(email=email_second_user)
        Logger.info("Set name")
        name_second_user = StringUtils.generate_random_string()
        registration_page.set_name(name=name_second_user)

        Logger.info("Go to login page")
        registration_page.click_button_sign_up()
        login_page = LoginPage()
        assert login_page.state.is_displayed() != True, "The login page should not open, you didn't enter your password"
        Logger.info("Test case 'test_registration_user_without_password' completed successfully")

    def test_login_user_without_password(self):
        Logger.info("Test case 'test_login_user_without_password' launched")
        Logger.info("Go to home page")
        home_page = HomePage()
        assert home_page.state.is_displayed(), "Home page is not open"

        Logger.info("Go to registration page")
        pages_menu = PagesMenu()
        pages_menu.go_to_registration_page()
        registration_page = RegistrationPage()
        assert registration_page.state.is_displayed(), "Registration page is not open."

        Logger.info("Registration user without name")
        Logger.info("Set email")
        email_third_user = StringUtils.generate_random_email()
        registration_page.set_email(email=email_third_user)
        Logger.info("Set password")
        password_third_user = StringUtils.generate_random_string()
        registration_page.set_password(password=password_third_user)

        Logger.info("Go to login page")
        registration_page.click_button_sign_up()
        login_page = LoginPage()
        assert login_page.state.is_displayed(), "Login page is not open."

        Logger.info("Login user without password")
        Logger.info("Set email")
        login_page.set_email(email=email_third_user)

        Logger.info("Go to profile page")
        login_page.click_button_login()
        profile_page = ProfilePage()
        assert profile_page.state.is_displayed() != True, "Profile page should not open, you didn't enter your password"
        Logger.info("Test case 'test_login_user_without_password' completed successfully")

    def test_login_user_with_false_password(self):
        Logger.info("Test case 'test_login_user_with_false_password' launched")
        Logger.info("Go to home page")
        home_page = HomePage()
        assert home_page.state.is_displayed(), "Home page is not open"

        Logger.info("Go to registration page")
        pages_menu = PagesMenu()
        pages_menu.go_to_registration_page()
        registration_page = RegistrationPage()
        assert registration_page.state.is_displayed(), "Registration page is not open."

        Logger.info("Registration user")
        Logger.info("Set email")
        email_fourth_user = StringUtils.generate_random_email()
        registration_page.set_email(email=email_fourth_user)
        Logger.info("Set name")
        name_fourth_user = StringUtils.generate_random_string()
        registration_page.set_name(name=name_fourth_user)
        Logger.info("Set password")
        password_fourth_user = StringUtils.generate_random_string()
        registration_page.set_password(password=password_fourth_user)

        Logger.info("Go to login page")
        registration_page.click_button_sign_up()
        login_page = LoginPage()
        assert login_page.state.is_displayed(), "Login page is not open. Incorrect registration"

        Logger.info("Login user")
        Logger.info("Set email")
        login_page.set_email(email=email_fourth_user)
        Logger.info("Set password")
        new_password = StringUtils.generate_random_string()
        login_page.set_password(password=new_password)

        Logger.info("Go to profile page")
        login_page.click_button_login()
        profile_page = ProfilePage()
        assert profile_page.state.is_displayed() != True, "Profile page should not open, you entered false password"
        Logger.info("Test case 'test_login_user_with_false_password' completed successfully")

    @pytest.mark.xfail
    def test_login_user_without_credentials(self):
        Logger.info("Test case 'test_login_user_without_credentials' launched")
        Logger.info("Go to home page")
        home_page = HomePage()
        assert home_page.state.is_displayed(), "Home page is not open"

        Logger.info("Go to login page")
        pages_menu = PagesMenu()
        pages_menu.go_to_login_page()
        login_page = LoginPage()
        assert login_page.state.is_displayed(), "Login page is not open."

        Logger.info("Login user without credentials")

        Logger.info("Go to profile page")
        login_page.click_button_login()
        profile_page = ProfilePage()
        assert profile_page.state.is_displayed() != True, "Profile page should not open, you didnt entered credentials"
        Logger.info("Test case 'test_login_user_without_credentials' completed successfully")
