violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

number_songs = int(input("Сколько песен выбрать? "))

duration_playlist = 0
for index in range(number_songs):
    name_song = input(f"Название {index + 1}-й песни: ")
    if name_song in violator_songs:
        duration_playlist += violator_songs[name_song]

print(f"\nОбщее время звучания песен: {duration_playlist:.2f} минуты")
