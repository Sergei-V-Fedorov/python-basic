number_records = int(input("Сколько записей вносится в протокол? "))
print("Записи (результат и имя):")

best_results = {}  # сохраняем только лучшие результаты каждого участника {name: (record, score), ...}
for number in range(1, number_records + 1):
    record = input(f"{number}-я запись: ")
    record = record.split()
    score = int(record[0])
    name = record[1]
    if name in best_results:
        previous_score = best_results[name]  # сравниваем с предыдущими результатами
        if score > previous_score[1]:  # переписываем, если они лучше
            best_results[name] = (number, score)
    else:
        best_results[name] = (number, score)

# сортировка по очкам по убыванию, по номеру записи по возрастанию [(name, (record, score))]
competition_results = sorted(best_results.items(),
                             key=lambda participant: (-participant[1][1], participant[1][0]))

print("\nИтоги соревнований:")
for position in range(1, 4):
    prize_winner = competition_results[position - 1][0]
    score = competition_results[position - 1][1][1]
    print(f"{position}-е место. {prize_winner} ({score})")
