import os


# определяет победителей этапа
def define_winners(tour_results):
    with open(tour_results, 'r') as ifile:
        passing_score = int(ifile.readline())
        tour_table = ifile.readlines()
    tour_table = [record.split() for record in tour_table]

    next_tour_table = []
    for participant in tour_table:
        if int(participant[-1]) > passing_score:
            new_record = (participant[1][:1] + ". " + participant[0], int(participant[-1]))
            next_tour_table.append(new_record)

    return next_tour_table


# формирует файл с протоколом соревнований
def write_tour_protocol(tour_results, tour_winners):
    participants = len(tour_winners)
    tour_winners.sort(key=lambda record: -record[1])

    with open(tour_results, 'w') as ofile:
        ofile.write(str(participants) + '\n')
        for ind, participant in enumerate(tour_winners, start=1):
            new_record = "{0}) {1} {2}\n".format(ind, *participant)
            ofile.write(new_record)


# вывод на печать содержимого файла
def print_text_file(target):
    short_name = os.path.split(target)
    with open(target, 'r') as text_file:
        user_text = text_file.read()
    print(f"Содержимое файла '{short_name[1]}':")
    print(user_text)


first_tour_results = "first_tour.txt"
second_tour_results = "second_tour.txt"

if os.path.exists(first_tour_results):
    print_text_file(first_tour_results)

    first_tour_winner = define_winners(first_tour_results)

    write_tour_protocol(second_tour_results, first_tour_winner)

    print()
    print_text_file(second_tour_results)
else:
    print(f"Файл '{first_tour_results}' не найден в текущей директории")
