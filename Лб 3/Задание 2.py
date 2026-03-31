# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):
    list1 = group1.split(separator)  # разбиваем строки на списки
    list2 = group2.split(separator)
    common = set(list1) & set(list2)  # находим пересечение
    return sorted(common)  # получаем отсортированный список


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, " ")
print(result)
# TODO Проверьте работу функции с разделителем отличным от запятой
