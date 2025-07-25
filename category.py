import openpyxl.workbook
import openpyxl
import aiohttp


class Category():
    def __init__(self, id, name, level_of_investigation, childs):
        self.id = id
        self.name = name
        self.level_of_investigation = level_of_investigation
        self.childs = childs

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.level_of_investigation}'


async def get_categories(url: str) -> list:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            data = data[2:]
            return data


def build_categories(nodes: list, level: int = 1) -> list[Category]:
    categories = []
    for node in nodes:
        children = build_categories(node.get('childs', []), level + 1)
        # если раскомментировать строку, то будет вложенность 99 для последних предметов
        # так нужно в тз, но я посчитал, что это не совсем корректно
        current_level = 99 if not children and level != 1 else level
        category = Category(
            id=node['id'],
            name=node['name'],
            level_of_investigation=current_level,  # current_level
            childs=children
        )
        categories.append(category)
    return categories


def print_categories(categories: list[Category], level: int = 0) -> None:
    for category in categories:
        print(f'{"  " * level}{category}')
        print_categories(category.childs, level + 1)


def write_categories_to_file(categories: list[Category], file_path: str) -> None:
    wb = openpyxl.Workbook()
    for category in categories:
        if not category.childs:
            continue
        ws = wb.create_sheet(title=category.name)

        def add_rows(childs: list[Category]):
            for cat in childs:
                ws.append([cat.id, cat.name, cat.level_of_investigation])
                add_rows(cat.childs)
        add_rows(category.childs)
    wb.save(file_path)
