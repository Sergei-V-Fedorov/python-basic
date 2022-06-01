class Cell:

    def __init__(self, number, is_free=True):
        self.is_free = is_free
        self.number = number


class Board:

    def __init__(self):
        self.cells = [Cell(index) for index in range(1, 10)]  # ячейки
        self.free_cells = list(range(1, 10))  # свободные ячейки
        # матрица отображения поля
        self.screen = [[str(column + 3*row + 1)
                        for column in range(3)]
                       for row in range(3)]

    def show_board(self):  # отображение поля
        for row in range(3):
            print(" | ".join(self.screen[row]))
            if row < 2:
                print("--+" + '-' * 3 + "+--")

    def make_move(self, num_cell, mark):
        if self.cells[num_cell - 1].is_free:
            self.cells[num_cell - 1].is_free = False  # занята
            self.free_cells.remove(num_cell)  # удаляем из свободных
            # ставим Х/0 на поле
            row, column = (num_cell - 1) // 3, (num_cell - 1) % 3
            self.screen[row][column] = mark
        else:
            print("Эта ячейка занята")

    def find_free(self):  # найти все свободные ячейки
        return [cell.number
                for cell in self.cells
                if cell.is_free]

    def if_fill_line(self, num_cell, mark):  # заполнена линия?
        row, column = (num_cell - 1) // 3, (num_cell - 1) % 3
        # проверка по строке, столбцу и диагоналям
        if all(cell == mark for cell in self.screen[row]):
            return True
        if all(cell == mark for cell in
               [self.screen[0][column], self.screen[1][column], self.screen[2][column]]):
            return True
        if row == column and all(cell == mark for cell in
                                 [self.screen[0][0], self.screen[1][1], self.screen[2][2]]):
            return True
        if row == (2 - column) and all(cell == mark for cell in
                                       [self.screen[0][2], self.screen[1][1], self.screen[2][0]]):
            return True
        return False


class Player:

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
