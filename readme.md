# Megatop Test Task
Скрипт для получения категорий и подкатегорий с wb и записи их в формат .xlsx
Техническое задание находится в папке ТЗ.docx

## Порядок запуска

1. Клонируйте репозиторий
```powershell
git clone https://github.com/backsterstockman/megatop_test_task
```

2. Установите зависимости
```powershell
pip install requirements.txt
```

3. Запустите приложение
```powershell
python main.py
```

## Результат работы вы можете наблюдать в файле categories.xlsx

## Дополнительное задание

Сборщик категорий с сайта был реализован асинхронно при помощи модуля aiohttp

Время выгрузки данных составило около 0.2 секунд

 