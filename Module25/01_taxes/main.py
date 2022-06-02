import taxes

total_money = int(input("Введите сумму доступных средств: "))
apartment_cost = int(input("Введите стоимость вашего жилья: "))
my_apartment = taxes.Apartment(apartment_cost)
car_cost = int(input("Введите стоимость вашего автомобиля: "))
my_car = taxes.Car(car_cost)
country_house_cost = int(input("Введите стоимость вашей дачи: "))
my_country_house = taxes.CountryHouse(country_house_cost)
apartment_tax = my_apartment.calculate_tax()
print("Величина налога на жилье составит:", apartment_tax)
car_tax = my_car.calculate_tax()
print("Величина налога на ТС составит:", car_tax)
country_house_tax = my_country_house.calculate_tax()
print("Величина налога на ТС составит:", country_house_tax)
total_taxes = apartment_tax + car_tax + country_house_tax
print("Суммарный налог на имущество составит:", total_taxes)
if total_money < total_taxes:
    print("Для уплаты налогов вам не хватает:", total_taxes - total_money)
else:
    print("У вас достаточно средств для уплаты налогов на имущество")
