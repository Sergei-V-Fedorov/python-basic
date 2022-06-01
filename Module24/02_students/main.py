import random
import students


names = ["Сидоренко А.И.", "Мартыч В.В.", "Раков И.А.", "Говоруха Н.В.", "Никитина А.А.",
        "Рубакина В.А.", "Морозов А.Н.", "Морозов А.Н.", "Павлюченко С.С.", "Конторович З.Э."]

random.shuffle(names)
excellent_students = students.StudentGroup()

for index in range(10):
    # заполняем данные на каждого студента
    group = random.randint(1, 3)
    marks = [random.randint(65, 100) for _ in range(5)]
    student = students.Student()
    student.name = names[index]
    student.group = group
    student.marks = marks

    # добавляем к группе
    excellent_students.add_to_group(student)

excellent_students.sort_students()  # сортируем по среднему баллу
excellent_students.print_info()  # выводим список студентов
