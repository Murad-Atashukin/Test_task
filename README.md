# Test home page

## Данный проект создан для тестирования ui сайта : "http://localhost:5000"

### Так как conftest.py находится не в директории tests, то для запуска тестов НЕОБХОДИМО директорию Test_task промаркировать, как - Test Sources Root, а директорию integrations/resources, как - Sources Root!

Для работы были использованы иструменты: Python, Selenium, фреймворк для автоматизированного тестирования на базе Selenium - py-selenium-auto "https://github.com/Polmik/py-selenium-auto". 

Было составлено 6 тест кейсов, тест кейс - "test_registration_user_without_password" и "test_login_user_without_credentials" - помечены как ожидаемо падающие, так как система неисправна. 

### Installation

1. Install requirements

```bash
pip install -r requirements.txt
```

2. Running tests

```bash
cd tests
```

```bash
pytest -v test_home_page.py
```
