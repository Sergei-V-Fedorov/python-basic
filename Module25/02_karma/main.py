# пример бестолково написанного задания, как хочешь, так и понимай
import random


def one_day():
    random_raises = ["KillError", "DrunkError", "CarCrashError", "GluttonyError", "DepressionError"]
    try:
        random_number = random.randint(1, 10)
        if random_number == 5:  # генерируется случайное событие вероятность выпадения числа 1/10
            msg = random.choice(random_raises)
            with open('karma.log', 'a') as ofile:
                ofile.write("Exception: " + msg + '\n')
            raise Exception(msg)
        else:
            return random.randint(1, 7)
    except:
        if msg == "KillError":
            print("Убийство плохо! Но даже взмах крыла бабочки, способен вызвать лавину случайных событий,"
                  "которые достигнут максимальной точки в другом месте и в другое время\n"
                  "Убитый человек стал бы президентом США, развязал 3 войны, приведших к гибели\n"
                  "тысяч человек и еще сотни тысяч, сделавших бедными и несчастными\n"
                  "Вместо того, чтобы переродиться жабой, вы получаете +50 к карме\n")
            return 50
        if msg == "CarCrashError":
            print("Убийство плохо! Но даже взмах крыла бабочки, способен вызвать лавину случайных событий,\n"
                  "которые достигнут максимальной точки в другом месте и в другое время\n"
                  "Убитый человек стал бы президентом США, развязал 2 войны, приведших к гибели"
                  "\nтысяч человек и еще сотни тысяч, сделавших бедными и несчастными\n"
                  "Вместо того, чтобы переродиться тараканом, вы получаете +50 к карме\n")
            return 50
        if msg == "DrunkError":
            print("Зло творит не алкоголь, а люди!\nВы напились в баре, ни с кем не подрались"
                  ", ничего не сломали. Тихо добрались домой и легли спать\n"
                  "Проснувшись, вы поняли, что и трезвость, и пьянство, это майя, иллюзии за которыми "
                  "скрывается сущность бытия.\nПоэтому ни то, ни другое не заслуживает внимания\n"
                  "Осознав это, вы получаете +50 к карме\n")
            return 50
        if msg == "GluttonyError":
            print("Чревоугодие такое же излишество, как и истязание тела голодом!\n"
                  "Буддизм не настаивает ни на каких ограничениях в пище, но и обжорство не одобряет\n"
                  "Умеренность и чистота помыслов. Только съев лишний килограмм пельменей вы это осознаете\n"
                  "И получаете +50 к карме\n")
            return 50
        if msg == "DepressionError":
            print("Депрессия - это состояние\nНа карму влияют только совершенные вами поступки.\n"
                  "Чтобы заесть депрессию, вы пошли в магазин за мороженным. На перекрестке вы помогли "
                  "перейти проезжую часть слепой женщине\n"
                  "Вы получаете +50 к карме\n")
            return 50


carma = 0
while True:

    bonus = one_day()
    carma += bonus
    if carma >= 500:
        print("Поздравляем! Вам удалось вырваться из океана Сансары")
        break
