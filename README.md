# Test home page

## Данный проект создан для тестирования ui сайта : "http://localhost:5000"

Для работы были использованы иструменты: Python, Selenium, фреймворк для автоматизированного тестирования на базе Selenium - py-selenium-auto "https://github.com/Polmik/py-selenium-auto". Было составлено 5 тест кейсов, тест кейс - "test_registration_user_without_password" - помечен как ожидаемо падающий. 
Так как conftest.py находится не в директории tests, то для запуска тестов НЕОБХОДИМО директорию Test_task промаркировать, как - Test Sources Root, а директорию integrations/resources, как - Sources Root!

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
