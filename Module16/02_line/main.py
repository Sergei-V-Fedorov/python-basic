class1 = list(range(160, 177, 2))
class2 = list(range(162, 181, 2))


def quick_sort(lst):  # сортировка списка
    return sorted(lst)

class1.extend(class2)

sorted_class = quick_sort(class1)
print("Отсортированный список учеников:", sorted_class)
