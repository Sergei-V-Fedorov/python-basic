from random import uniform

length = 20
low = 5
up = 10

first_team = [round(uniform(low, up), 2) for _ in range(length)]
second_team = [round(uniform(low, up), 2) for _ in range(length)]

winners = [max(participants[0], participants[1]) for participants in zip(first_team, second_team)]

print("Первая команда:", first_team)
print("Вторая команда:", second_team)
print("Победители тура:", winners)
