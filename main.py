from dotenv import load_dotenv
import os
from category import build_categories, get_categories, print_categories, write_categories_to_file

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

    url = os.getenv('URL')
    data = get_categories(url)
    categories = build_categories(data)
    print_categories(categories)
    print(f'Всего категорий верхнего уровня: {len(categories)}')
    for cat in categories:
        print(f'{cat.name}: {len(cat.childs)} дочерних')
    write_categories_to_file(categories, 'categories.xlsx')
