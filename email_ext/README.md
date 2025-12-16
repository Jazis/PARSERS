# Email Extractor (email_ext)

## 📝 Описание

Специализированный веб-краулер для целенаправленного поиска и извлечения email-адресов с веб-сайтов. Сканирует сайт, ищет `mailto:` ссылки и извлекает валидные email-адреса.

## 🎯 Назначение

- Рекурсивное сканирование веб-сайта
- Поиск mailto: ссылок
- Извлечение и валидация email-адресов
- Фильтрация по домену
- Автоматический сбор контактов

## 📋 Файлы

- **`spider.py`** - Основной краулер для извлечения email
- **`tururu.py`** - Дополнительный скрипт обработки
- **`base.txt`** - Базовые URL для старта
- **`temp0`** - Временное хранилище HTML
- **`output/`** - Результаты работы
  - `emails.txt` - Найденные email-адреса
  - `urls.txt` - Все посещенные URL
  - `extract.py` - Скрипт обработки результатов
  - `params.txt` - Извлеченные параметры
- **`login_base/`** - Обработка форм входа
  - `login_base.py` - Парсер форм логина
  - `out.txt` - Результаты

## 🔧 Требования

```bash
pip install requests
```

## 🚀 Использование

### Запуск

```bash
python spider.py
```

### Интерактивный ввод

```
Input site
URL which you want -> http://www.fa.ru/university/
```

## 📊 Как работает

### 1. Инициализация
```python
site = input('URL which you want -> ')
site00 = site.split('/')[2].split('.')[-2]  # Домен
```

### 2. Поиск mailto: ссылок
```python
if 'mailto:' in line:
    # Извлекает email из ссылки
    new_line1 = line.split('"')[i].split(':')[1].split('>')[0]
```

### 3. Валидация email
```python
if ' ' in new_line1:
    pass  # Пропускает с пробелами
else:
    if '@' in new_line1 and '.' in new_line1:
        # Валидный email
```

### 4. Фильтрация дубликатов
```python
if new_line1 in app_words:
    pass
else:
    app_words.append(new_line1)
    temp2_save.write(new_line1 + '\n')
```

### 5. SSL обработка
```python
try:
    req1 = requests.get(sites_score[x])
except requests.exceptions.SSLError:
    pass  # Пропускает проблемные сайты
```

## 📈 Пример работы

### Запуск
```bash
python spider.py
Input site
URL which you want -> http://university.edu/contacts
```

### Процесс
```
15[3][2]
Найдено: admin@university.edu
28[7][5]
Найдено: info@university.edu
42[12][8]
Найдено: support@university.edu
```

### Результат

#### output/emails.txt
```
admin@university.edu
info@university.edu
support@university.edu
admissions@university.edu
pr@university.edu
```

#### output/urls.txt
```
http://university.edu/contacts
http://university.edu/about
http://university.edu/departments
```

## 🔍 Особенности

### Валидация email
- Проверяет наличие `@`
- Проверяет наличие `.`
- Исключает адреса с пробелами
- Фильтрует дубликаты

### Обработка mailto:
```html
<!-- Находит email из таких ссылок -->
<a href="mailto:contact@example.com">Contact Us</a>
<a href="mailto:info@example.com?subject=Question">Info</a>
```

### SSL Error handling
Автоматически пропускает сайты с проблемами SSL сертификатов.

### Счетчики
```python
print str(len(sites_score)) + str([count]) + str([count2])
# [Всего URL][Внутренние ссылки][Попытки извлечения email]
```

## 💡 Применение

### Сбор контактов организации
```bash
python spider.py
URL which you want -> http://company.com/about/team
# Находит все email сотрудников
```

### Поиск email для маркетинга
```bash
python spider.py
URL which you want -> http://business-directory.com/
# Собирает контакты для B2B
```

### Аудит сайта
```bash
python spider.py
URL which you want -> http://mywebsite.com/
# Проверяет все публичные email
```

## 🐛 Решение проблем

### Проблема: Email не найдены
**Решение:**
- Проверьте наличие mailto: на сайте
- Некоторые сайты скрывают email через JavaScript
- Попробуйте страницу контактов

### Проблема: SSL ошибки
**Решение:**
```python
# Отключить проверку SSL (небезопасно!)
requests.get(url, verify=False)
```

### Проблема: Блокировка сайтом
**Решение:**
- Добавьте задержки
- Используйте реальный User-Agent
- Смените IP через прокси

### Проблема: Неполные email
**Решение:**
Проверьте алгоритм извлечения, возможно нужна доработка парсинга.

## 💡 Улучшения

### 1. Расширенный поиск email
```python
import re

# Ищет email не только в mailto:
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, html_text)
```

### 2. Валидация через библиотеку
```python
from email_validator import validate_email, EmailNotValidError

try:
    valid = validate_email(email)
    email = valid.email  # Нормализованный email
except EmailNotValidError as e:
    print(f"Invalid email: {e}")
```

### 3. Обфусцированные email
```python
# Находит email вида: user [at] example [dot] com
obfuscated = r'\w+\s*\[at\]\s*\w+\s*\[dot\]\s*\w+'
```

### 4. JavaScript-rendered email
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
# Теперь можно найти JS-generated email
```

### 5. Логирование
```python
import logging
logging.basicConfig(
    filename='email_extraction.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)
```

## 🔄 Миграция на Python 3

```python
# Было (Python 2)
print 'Input site'
site = raw_input('URL which you want -> ')

# Стало (Python 3)
print('Input site')
site = input('URL which you want -> ')
```

## 📊 Статистика

### Добавить детальный отчет
```python
stats = {
    'total_pages_scanned': len(sites_score),
    'unique_emails': len(app_words),
    'internal_links': count,
    'mailto_links_found': count2
}

print(f"\nСтатистика:")
print(f"Страниц просканировано: {stats['total_pages_scanned']}")
print(f"Уникальных email: {stats['unique_emails']}")
print(f"Внутренних ссылок: {stats['internal_links']}")
```

## 🔒 GDPR и конфиденциальность

⚠️ **ВАЖНО:**
- Email = персональные данные по GDPR
- Требуется законное основание для сбора
- Нельзя использовать для спама
- Соблюдайте право на забвение

### Легальные основания:
- ✅ Публичные контакты организаций
- ✅ B2B email для бизнес-целей
- ✅ С согласия владельца
- ❌ Массовая рассылка без согласия
- ❌ Продажа баз email

## 📝 Примеры команд

### Сбор с университетского сайта
```bash
python spider.py
URL which you want -> http://university.edu/faculty
```

### Сбор с бизнес-каталога
```bash
python spider.py
URL which you want -> http://business-directory.com/companies
```

### Проверка своего сайта
```bash
python spider.py
URL which you want -> http://mycompany.com/
```

## 🧹 Очистка результатов

### Удаление дубликатов (дополнительно)
```python
# В output/
with open('emails.txt', 'r') as f:
    emails = set(f.readlines())

with open('emails_unique.txt', 'w') as f:
    f.writelines(sorted(emails))
```

### Фильтрация по домену
```python
# Только .edu email
edu_emails = [e for e in emails if '.edu' in e]
```

## 🔗 Связанные инструменты

- **domain_email_scraper/** - Поиск email по конкретному домену
- **dork_url_crawler/** - Для генерации URL списков
- **basic_web_crawler/** - Базовый сбор URL

## 📚 Дополнительные ресурсы

- [Email Validation RFC 5322](https://tools.ietf.org/html/rfc5322)
- [GDPR Email Guidelines](https://gdpr.eu/email-encryption/)
- [Python email-validator](https://pypi.org/project/email-validator/)

---

**Автор:** Jazis  
**Версия:** 1.0  
**Python:** 2.7 (рекомендуется обновление до 3.x)  
**Статус:** Соблюдайте GDPR и локальные законы  
**Последнее обновление:** 16 декабря 2025
