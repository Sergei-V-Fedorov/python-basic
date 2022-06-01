import random
import CrossesAndZeroes as cz

new_game = cz.Board()

player_1 = cz.Player("Sergei", 'X')
player_2 = cz.Player("Computer", '0')

while True:
    new_game.show_board()

    choice = int(input("Введите номер клетки: "))  # ход игрока
    if not new_game.cells[choice - 1].is_free:  # если клетка занята, повторить
        continue
    new_game.make_move(choice, player_1.mark)  # заполнить поле
    if new_game.if_fill_line(choice, player_1.mark):
        print(f"{player_1.name} выиграл!!!")
        break

    if not new_game.free_cells:  # нет свободных
        print("Свободных ячеек нет. Ничья!!!")
        break

    choice = random.choice(new_game.free_cells)  # ход компа: выбрать свободную ячейку
    new_game.make_move(choice, player_2.mark)  # заполнить поле
    if new_game.if_fill_line(choice, player_2.mark):
        print(f"{player_2.name} выиграл!!!")
        break

new_game.show_board()
