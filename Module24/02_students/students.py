class Student:

    def __init__(self):
        self.name = None
        self.group = None
        self.marks = None


class StudentGroup:

    def __init__(self):
        self.group = []

    def add_to_group(self, new_student):
        self.group.append(new_student)

    def print_info(self):
        print("==== Успеваемость по курсу Python Basics ====")
        for some_student in self.group:
            if some_student.marks:
                print("{0} группа {1}\t средний балл:  {2:.2f}".format(
                    some_student.name.ljust(20),
                    some_student.group,
                    sum(some_student.marks) / len(some_student.marks)))

    def sort_students(self):
        self.group = sorted(self.group,
                            key=lambda some_student: -(sum(some_student.marks) / len(some_student.marks)))
