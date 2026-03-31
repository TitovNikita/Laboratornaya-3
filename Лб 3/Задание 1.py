# TODO Напишите функцию для поиска индекса товара
def find_index(item, index):  # сравнение фруктов в исходном и новом списках и вывод индекса в случае совпадения
    for i, value in enumerate(item):
        if value == index:
            return i
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']  # исходный список

for find_item in ['банан', 'груша', 'персик']:  # новый список
    index_item = find_index(items_list, find_item)  # вызываем функцию для каждого фрукта в новом списке
    if index_item is not None:  # если товар найден, то получим его индекс
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
