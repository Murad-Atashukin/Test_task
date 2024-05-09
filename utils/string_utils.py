import string
import random
from py_selenium_auto_core.logging.logger import Logger


class StringUtils:

    @staticmethod
    def generate_random_string(len_string=10):
        Logger.info("Генерация случайной строки")
        characters = string.ascii_letters
        random_string = ''.join(random.choice(characters) for _ in range(int(len_string)))
        return random_string

    @staticmethod
    def generate_random_email(len_email=5):
        Logger.info("Генерация случайного логина")
        characters = string.ascii_letters
        random_string = ''.join(random.choice(characters) for _ in range(int(len_email)))
        random_string = random_string + '@' + random_string
        return random_string
