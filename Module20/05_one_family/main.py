# склонение фамилии по родам
def declension_by_gender(user_name):
    if user_name.endswith("ая") or user_name.endswith("ий"):
        return user_name[:-2] + "ий", user_name[:-2] + "ая"
# здесь проблема, т.к. может быть 2 варианта окончаний муж.фамилии (...ий, ...ый) - ...ая
#    elif user_name.endswith("ая") or user_name.endswith("ый"):
#        return user_name[:-2] + "ый", user_name[:-2] + "ая"
    elif user_name.endswith("в") or user_name.endswith("ин"):
        return user_name, user_name + "а"
    elif user_name.endswith("ва") or user_name.endswith("ина"):
        return user_name[:-1], user_name
    else:
        return user_name, user_name


family_info = {
    ("сидоров", "никита"): 35,
    ("сидорова", "алина"): 34,
    ("сидоров", "павел"): 10,
    ("сидоровский", "руслан"): 36,
    ("сидоровская", "анжела"): 38,
    ("мосин", "николай"): 48,
    ("мосина", "лариса"): 45,
    ("мосина", "любовь"): 20,
    ("носик", "антон"): 32,
    ("носик", "антонина"): 32,
    ("носик", "антошка"): 4
}

surnames = set(key[0] for key in family_info)  # оригинальные фамилии

request = input("Введите фамилию: ").lower()
print()

if request in surnames:
    # муж/жен версии фамилии
    male_surname, female_surname = declension_by_gender(request)
    for person, age in family_info.items():
        if person[0] == male_surname or person[0] == female_surname:
            print(person[0].capitalize(), person[1].capitalize(), age)
else:
    print("Нет такой фамилии в базе данных :(")
