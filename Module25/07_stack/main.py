import stack

my_stack = stack.Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("В стэке:", my_stack)  # 3, 2, 1
a = my_stack.peek()  # 3
print("Головной элемент:", a)
b = my_stack.pop()  # 3
print("Удаление головного элемента:", b)
print("После удаления стэк:", my_stack)  # 2, 1

# task manager
print("\ntask manager test")
manager = stack.TaskManager()
manager.new_task("написать Гвидо", 2)
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("сходить в магазин", 3)
manager.new_task("отдохнуть", 1)
manager.new_task("написать Гвидо", 3)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
