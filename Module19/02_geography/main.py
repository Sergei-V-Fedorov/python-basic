number_countries = int(input("Количество стран: "))

geography_db = {}
for index in range(number_countries):
    country_info = input(f"{index + 1}-ая страна: ").split()
    geography_db[country_info[0]] = country_info[1:]

for request in range(3):
    city_name = input(f"\n{request + 1}-й город: ")

    present_in_db = any(city_name in value
                        for value in geography_db.values())
    if present_in_db:
        for key, value in geography_db.items():
            if city_name in value:
                print(f"Город {city_name} расположен в стране {key}.")
    else:
        print(f"По городу {city_name} данных нет.")
