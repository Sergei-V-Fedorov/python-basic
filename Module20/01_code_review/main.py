students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# возвращает полный список интересов всех студентов и общую длину всех фамилий
def select_interest_length_surname(original_dictionary):
    surnames = [len(original_dictionary[key]["surname"])
                for key in original_dictionary
                if "surname" in original_dictionary[key]]
    sum_surname = sum(surnames)

    interests = [interest
                 for key in original_dictionary
                 for interest in original_dictionary[key]["interests"]
                 if "interests" in original_dictionary[key]]
    return set(interests), sum_surname


id_and_age = [(ids, students[ids]["age"])
              for ids in students
              if "age" in students[ids]]
print('Список пар "ID студента — возраст":', id_and_age)

students_interests, students_surname_length = select_interest_length_surname(students)
print("Полный список интересов всех студентов:", students_interests)
print("Общая длина всех фамилий студентов:", students_surname_length)
