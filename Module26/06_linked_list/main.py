from typing import Any, Optional


class Node:

    def __init__(self, data: Optional[Any] = None, reference: Optional['Node'] = None) -> None:
        self.data = data
        self.next = reference

    def __str__(self) -> str:  # use for test
        return str(self.data)


class SinglyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.__length = 0
        self.__index = 1  # для итератора

    def append(self, data: Optional[Any]) -> None:
        new_node = Node(data)
        if self.__length:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        else:
            self.head = new_node
        self.__length += 1

    def get(self, index: int) -> Optional[Any]:
        if self.__length and 1 <= index <= self.__length:
            current_node = self.head
            while index > 1:
                current_node = current_node.next
                index -= 1
            return current_node.data
        else:
            raise IndexError

    def remove(self, index: int) -> None:
        if self.__length and 1 <= index <= self.__length:
            previous_node = None
            current_node = self.head

            for _ in range(1, index):  # для index > 1
                previous_node = current_node  # узел перед удаляемым
                current_node = previous_node.next  # удаляемый узел

            self.__length -= 1

            if previous_node:  # не голова
                current_node = current_node.next  # на место удаляемого ставим след.узел
                previous_node.next = current_node  # предыдущий узел ссылается на новый узел
            else:  # голова
                self.head = current_node.next  # на место удаляемого ставим след.узел
        else:
            raise IndexError

    def __str__(self) -> str:  # формат вывода [x1, x2, x3] выглядит лучше, чем [x1 x2 x3]
        result = self.__get_iterable()
        return str(result)

    def __get_iterable(self) -> list:  # it maybe used as iterator via iter()git
        return [self.get(index)
                for index
                in range(1, self.__length + 1)]

    def __iter__(self):
        return self

    def __next__(self) -> Optional[Any]:
        if self.__index > self.__length:
            self.__index = 1
            raise StopIteration
        else:
            result = self.get(self.__index)
            self.__index += 1
            return result


my_list = SinglyLinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

print("Перебор эл-ов в цикле:")
for node in my_list:
    print(node, end=' ')

print('\nТекущий список:', my_list)
print('Получение третьего элемента:', my_list.get(3))
print('Удаление второго элемента.')
my_list.remove(2)
print('Новый список:', my_list)
