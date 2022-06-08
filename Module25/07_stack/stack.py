class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.insert(0, element)

    def __str__(self):
        return ", ".join(str(i) for i in self.stack)

    def peek(self):
        return self.stack[0]

    def pop(self):
        return self.stack.pop(0)


class TaskManager:

    def __init__(self):
        self.tasks = []
        self.priority = []
        self.task_dict = {}


    def new_task(self, task_name, priority):
        if task_name in self.tasks:  # проверка на дубли
            index = self.tasks.index(task_name)  # удаляем старое задание
            self.priority.pop(index)
            self.tasks.remove(task_name)
        self.tasks.insert(0, task_name)
        self.priority.insert(0, priority)
        '''if priority in self.task_dict:
            self.task_dict[priority].insert(0, task_name)
        else:
            self.task_dict[priority] = [task_name]'''

    def __task_2_dict(self):  # преобразование в словарь
        result = {}
        # последний пришел, первый вышел
        for priority, task in zip(self.priority[::-1], self.tasks[::-1]):
            if priority in result:
                result[priority].insert(0, task)
            else:
                result[priority] = [task]
        return result

    def peek(self):
        return self.tasks[0], self.priority[0]

    def pop(self):
        return self.tasks.pop(0), self.priority[0].pop(0)

    def __str__(self):
        task_dict = self.__task_2_dict()
        result = [str(key) + ' ' + '; '.join(task_dict[key]) + '\n'
                  for key in sorted(task_dict)]
        return ''.join(result)
