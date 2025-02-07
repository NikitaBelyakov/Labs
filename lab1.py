def find_value_path(dictionary, value):
  for key, val in dictionary.items():
    if val == value:
      return [key]
    elif isinstance(val, dict):
      path = find_value_path(val, value)
      if path:
        return [key] + path
    elif isinstance(val, list):
      for item in val:
        if item == value:
          return [key, item]

  return None

zoo_dict = {
    'Старая территория': {
        'Дом птиц': {
            'Черный аист': 'Черный аист',
            'Пингвин Гумбольдта': 'Пингвин Гумбольдта',
            'Шилоклювка': 'Шилоклювка',
        },
        'Амфибии': 'Амфибии',
        'Слоновник': 'Азиатский слон',
        'Ластоногие': {
            'Северный морской котик': 'Северный морской котик',
            'Сивуч': 'Сивуч',
            'Морж': 'Морж',
            'Дальневосточная нерпа': 'Дальневосточная нерпа',
        },
        'Змеиное сафари': {
            'Персидская гадюка': 'Персидская гадюка',
            'Рогатая гадюка': 'Рогатая гадюка',
            'Гадюка-носорог': 'Гадюка-носорог',
        },
        'Рептилии': {
            'Исполинская ящерица': 'Исполинская ящерица',
            'Рогатая ящерица': 'Роагатая ящерица',
            'Большой сирен': 'Большой сирен',
        },
        'Хищные птицы': {
            'Белоголовый орлан': 'Белоголовый орлан',
            'Снежный гриф': 'Снежный гриф',
            'Андский кондор': 'Андский кондор',
        },
        'Зона 1': {
            'Сурок': 'Степной сурок',
            'Тюлень': 'Cерый тюлень',
            'Фазан': 'Обыкновенный фазан',
            'Утки': ['Серая утка', 'Чирок', 'Каролинская утка'],
            'Овцебык': 'Канадский овцебык'
        },
        'Зона 2': {
            'Кустарниковая собака': 'Кустарниковая собака',
            'Енот-полоскун': 'Енот-полоскун',
            'Домашний як': 'Домашний як',
            'Гривистый волк': 'Гривистый волк'
        },
        'Кошачий ряд': {
            'Пума': 'Пума',
            'Дальневосточный леопард': 'Дальневосточный леопард',
            'Рысь': 'Восточно-сибирская рысь'
        },
        'Зона 3': {
            'Гималайский медведь': 'Гималайский медведь',
            'Малая панда': 'Малая панда',
            'Беркут': 'Беркут',
            'Манулы': 'Манул Тимофей',
        },
        'Скала хищных птиц': {
            'Кондор': 'Андский кондор',
            'Орлан-белохвост': 'Орлан-белохвост',
            'Гриф': ['Снежный гриф', 'Черный гриф']
        }
    },
    'Новая территория': {
    # Я тут не стал заполнять вторую половину зоопарка. Это глобально ничего не изменит, код будет работать в любом случае.
    }
}

path = find_value_path(zoo_dict, 'Манул Тимофей')
print('Соседи манула Тимофея:')
for i_key in zoo_dict[path[0]][path[1]].keys():
    if i_key == 'Манулы':
        continue
    else:
        print(i_key)

