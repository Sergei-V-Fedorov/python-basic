import black_jack as bj


player_1 = bj.Player("Sergei")
player_2 = bj.Player("Dealer")

new_deck = bj.Deck()
new_deck.deck_shuffle()  # перетасовать

for player in (player_1, player_2):  # раздаем по 2 карты
    for _ in range(2):
        new_card = new_deck.take_card()
        player.add_card(new_card)

while True:
    player_1.show_hand()
    print("Вы набрали:", player_1.calc_score())

    player_choice = input("\nВзять карту или остановиться (0/1)? ")
    if player_choice.isdigit():
        if player_choice == '0':
            new_card = new_deck.take_card()
            print(player_2.name, "сдает:", new_card.show_card())
            player_1.add_card(new_card)
        else:
            for player in (player_1, player_2):
                player.show_hand()
                print(f"{player.name} набрал", player.calc_score(), "очков")
            player_1_score = player_1.calc_score()
            if player_1_score > 21:
                print(f"Перебор! {player_2.name} выиграл!")
            else:
                player_2_score = player_2.calc_score()
                if player_2_score > player_1_score:
                    print(f"{player_2.name} выиграл!")

                elif player_2_score < player_1_score:
                    print("Поздравляем, вы выиграли!")
                else:
                    print("Ничья")
            break
    else:
        print("Неправильный ввод")
