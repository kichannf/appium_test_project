# Учеба/Практика автоматизации тестирования МП.
## **Тема:** "Appium"

---------
### Цели:
- Разобраться с Appium на python
- Написать тесты

### APK:
**Habita** - приложение создания и отслеживания привычек  
_[Path к apk](src/apk)_

### Выполнено:
1. [Базовый класс](src/pages/base_page.py) и [пейджи](src/pages)
2. [Локаторы](src/locators)
3. pytest.ini - настройка конфигурации pytest.
4. conftest.py
5. requirements.txt - зависимости
6Необходимо добавить в корень проекта файл `.env`
6. Добавлен Allure

### Предусловия запуска:
    Примечание: на данный момент запускал только в эмуляторе
1. Запустить эмулятор в Android Studio
2. Запустить Appium

### Запуск:
1. Тесты можно запустить локально:
   - Из модулей отдельно каждый тест или класс.
   - Через командную строку локально:  
     `pytest`
2. Для создания отчета allure:
    - allure-result генерируется автоматически при запуске тестов.
    - В консоли запустить:  `[Путь до allure] generate [путь до allure-results] allure-results/`
      - Мой пример: `C:/Users/user/Downloads/allure-2.29.0/bin/allure.bat generate allure-results/`
    - Подождать создания allure-report.
    - В папке allure-report открыть файл index.html, откроется отчет в браузере.

### Инструменты:
- python 3.12
- pytest
- appium
- allure
- python-dotenv

### Линтер:
- flake8

---------

### Автор: Кичан Николай
