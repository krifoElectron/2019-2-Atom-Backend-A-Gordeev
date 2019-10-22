class X_0:
    def __init__(self):
        self.field = '''             |     |
          0  |  1  |  2
        _____|_____|_____
             |     |
          3  |  4  |  5
        _____|_____|_____
             |     |
          6  |  7  |  8
             |     |   '''
        self.stroke_number = 0
        self.matrix = [[None for _ in range(3)] for _ in range(3)]
        self.player_now = None
        self.win0 = False
        self.win1 = False

        self.print_field()

        self.who_a_u()
        self.play(self.next())

    def who_a_u(self):
        self.name0 = input('0 игрок, как тебя зовут? ')
        self.name1 = input('1 игрок, как тебя зовут? ')

    def play(self, player):
        self.make_move(player)
        self.print_field()
        self.check(player)
        self.maybe_all()

    def print_field(self):
        print(self.field)

    def make_move(self, player):
        num = input(
            f'игрок {self.name1 if player else self.name0}, сделайте ход: ')
        num = num.strip()
        pos = self.field.find(num)
        if pos == -1 or num == '':
            print('введите правильный номер ячейки!')
            self.make_move(player)
            return

        self.stroke_number += 1
        x_or_0 = 'X' if player == 0 else 'O'
        self.field = self.field.replace(num, x_or_0)
        self.matrix[int(num) // 3][int(num) % 3] = x_or_0

    def exit(self):
        print('эт всё')

    def check(self, player):
        x_or_0 = 'X' if player == 0 else 'O'
        is_win = False

        for i in range(3):
            is_win_temp = True
            for j in range(3):
                if self.matrix[i][j] != x_or_0:
                    is_win_temp = False
            if is_win_temp:
                is_win = True

        for i in range(3):
            is_win_temp = True
            for j in range(3):
                if self.matrix[j][i] != x_or_0:
                    is_win_temp = False
            if is_win_temp:
                is_win = True

        is_win_temp = True
        for i in range(3):
            if self.matrix[i][i] != x_or_0:
                is_win_temp = False
        if is_win_temp:
            is_win = True

        is_win_temp = True
        for i in range(3):
            if self.matrix[i][2 - i] != x_or_0:
                is_win_temp = False
        if is_win_temp:
            is_win = True

        if is_win:
            if player == 0:
                self.win0 = True
            else:
                self.win1 = True

    def next(self):
        if self.player_now == 0:
            self.player_now = 1
        else:
            self.player_now = 0
        return self.player_now

    def maybe_all(self):
        if self.win0:
            print(f'игрок {self.name0} подедил!')
            self.exit()
        elif self.win1:
            print(f'игрок {self.name1} подедил!')
            self.exit()
        elif self.stroke_number == 9:
            print('ничья...')
            self.exit()
        else:
            self.play(self.next())


game = X_0()
