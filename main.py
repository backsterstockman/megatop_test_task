from dotenv import load_dotenv
import os
from category import build_categories, get_categories, print_categories, write_categories_to_file
import asyncio
import time


async def main():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

        url = os.getenv('URL')

        start = time.time()
        data = await get_categories(url)
        end = time.time()
        print(f"Время получения данных: {end - start} секунд")

        categories = build_categories(data)
        # print_categories(categories)
        write_categories_to_file(categories, 'categories.xlsx')


if __name__ == "__main__":
    asyncio.run(main())
