**Что такое системные пути (PATH)?**
Системный путь (PATH) — это список папок, где операционная система ищет программы. Например:
- Когда вы пишете `python` в терминале, система ищет исполняемый файл Python в папках из PATH.
- Если драйвер (например, `chromedriver`) не находится в PATH, его нужно запускать через полный путь: `/Users/.../chromedriver`.

**Как добавить папку в PATH:**
- **macOS/Linux:**
  1. Откройте терминал.
  2. Добавьте путь в конец файла `~/.bashrc`, `~/.zshrc` (зависит от вашей оболочки):
     ```bash
     export PATH=$PATH:/путь/к/папке/с/драйвером
     ```
  3. Перезагрузите конфигурацию: `source ~/.zshrc` (или `source ~/.bashrc`).

- **Windows:**
  1. Откройте "Параметры системы" → "Дополнительные параметры" → "Переменные среды".
  2. В разделе "Системные переменные" найдите переменную `Path` и добавьте новую строку с путем к папке с драйвером.

Чтобы код работал локально и соответствовал мог запускаться на сервере, нужно:
1. **Установить Google Chrome и ChromeDriver** .
2. **Добавить ChromeDriver в PATH** (чтобы не указывать путь в коде).

 **Шаг 1: Установите Google Chrome**
- Скачайте Chrome с [официального сайта](https://www.google.com/chrome/).
- Убедитесь, что он открывается через терминал: `google-chrome --version`.

**Шаг 2: Установите ChromeDriver**
1. Скачайте драйвер с [официального сайта](https://googlechromelabs.github.io/chrome-for-testing/). Версия должна совпадать с версией Chrome.
2. Распакуйте архив. Вы увидите файл `chromedriver` (macOS/Linux) или `chromedriver.exe` (Windows).
3. **Добавьте папку с драйвером в PATH** (как описано выше).

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Создаем опции для Chrome
    options = Options()
    options.add_argument("--window-size=1200,600")  # Задаем размер окна
    
    # Инициализируем драйвер (путь к нему должен быть в PATH)
    driver = webdriver.Chrome(options=options)
    
    yield driver
    driver.quit()
```

**Проверьте работу**
Запустите тесты:
```bash
pytest
```
Если всё настроено правильно, Chrome запустится с размером окна `1200x600`.