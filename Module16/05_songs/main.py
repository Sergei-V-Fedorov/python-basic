violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


#  расчет продолжительности нового плейлиста
def duration(playlist, song_names):
    # список продолжительности песен из списка song_names
    result = [item[1] for item in playlist if item[0] in song_names]
    return sum(result)


new_songs = []  # формируем список новых песен
quantity = int(input("Сколько песен выбрать? "))
for index in range(quantity):
    new_songs.append(input(f"Название {index + 1}-й песни: "))

count = duration(violator_songs, new_songs)

print(f"\nОбщее время звучания песен: {count:.2f} минуты")
