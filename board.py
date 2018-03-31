import copy
from var_dump import var_dump


class Board:
    tabela = [[None, None, None], [None, None, None], [None, None, None]]
    size = 3

    def __init__(self, table):
        self.tabela = table

    def setTable(self, table):
        self.tabela = table

    def getTable(self):
        return self.tabela

    def clean(self):
        for i in range(self.size):
            for j in range(self.size):
                self.tabela[i][j] = ""

    def printer(self):
        for i in range(self.size):
            print(self.tabela[i][0] + " | " + self.tabela[i][1] + " | " +
                  self.tabela[i][2])

    def mark(self, mark, line, colm):
        self.tabela[line][colm] = mark

    def how_many_times_i_can_lose(self):
        count = 0
        auxTable = copy.deepcopy(self.tabela[:])
        for i in range(self.size):
            for j in range(self.size):
                if auxTable[i][j] == "X":
                    auxTable[i][j] = 1
                else:
                    auxTable[i][j] = -1

        for i in range(self.size):
            if (auxTable[i][0] + auxTable[i][1] +
                    auxTable[i][2]) == -3:
                count = count + 1

        for i in range(self.size):
            if (auxTable[0][i] + auxTable[1][i] +
                    auxTable[2][i]) == -3:
                count = count + 1

        if (auxTable[0][0] + auxTable[1][1] +
                auxTable[2][2]) == -3:
            count = count + 1

        if (auxTable[0][2] + auxTable[1][1] +
                auxTable[2][0]) == -3:
            count = count + 1
        return count
    def where_i_win(self):
        auxTable = copy.deepcopy(self.tabela[:])
        for i in range(self.size):
            for j in range(self.size):
                if auxTable[i][j] == "X":
                    auxTable[i][j] = 1
                elif auxTable[i][j] == "O":
                    auxTable[i][j] = -1
                else:
                    auxTable[i][j] = 0
        # Linha
        for i in range(self.size):
            if (auxTable[i][0] + auxTable[i][1] +
                    auxTable[i][2]) == 2:
                if auxTable[i][0] == 0:
                    return [i, 0]
                elif auxTable[i][1] == 0:
                    return [i, 1]
                else:
                    return [i, 2]
        # Coluna
        for i in range(self.size):
            if (auxTable[0][i] + auxTable[1][i] +
                    auxTable[2][i]) == 2:
                if auxTable[0][i] == 0:
                    return [0, i]
                elif auxTable[1][i] == 0:
                    return [1, i]
                else:
                    return [2, i]
        # Diagonal Principal
        if (auxTable[0][0] + auxTable[1][1] + auxTable[2][2]) == 2:
            if auxTable[0][0] == 0:
                return [0, 0]
            elif auxTable[1][1] == 0:
                return [1, 1]
            else:
                return [2, 2]
        # Diagonal Secundaria
        if (auxTable[0][2] + auxTable[1][1] + auxTable[2][0]) == 2:
            if auxTable[0][2] == 0:
                return [0, 2]
            elif auxTable[1][1] == 0:
                return [1, 1]
            else:
                return [2, 0]
        return False

    def where_i_lose(self):
        auxTable = copy.deepcopy(self.tabela[:])
        for i in range(self.size):
            for j in range(self.size):
                if auxTable[i][j] == "O":
                    auxTable[i][j] = 1
                elif auxTable[i][j] == "X":
                    auxTable[i][j] = -1
                else:
                    auxTable[i][j] = 0
        # Linha
        for i in range(self.size):
            if (auxTable[i][0] + auxTable[i][1] +
                    auxTable[i][2]) == 2:
                if auxTable[i][0] == 0:
                    return [i, 0]
                elif auxTable[i][1] == 0:
                    return [i, 1]
                else:
                    return [i, 2]
        # Coluna
        for i in range(self.size):
            if (auxTable[0][i] + auxTable[1][i] +
                    auxTable[2][i]) == 2:
                if auxTable[0][i] == 0:
                    return [0, i]
                elif auxTable[1][i] == 0:
                    return [1, i]
                else:
                    return [2, i]
        # Diagonal Principal
        if (auxTable[0][0] + auxTable[1][1] + auxTable[2][2]) == 2:
            if auxTable[0][0] == 0:
                return [0, 0]
            elif auxTable[1][1] == 0:
                return [1, 1]
            else:
                return [2, 2]
        # Diagonal Secundaria
        if (auxTable[0][2] + auxTable[1][1] + auxTable[2][0]) == 2:
            if auxTable[0][2] == 0:
                return [0, 2]
            elif auxTable[1][1] == 0:
                return [1, 1]
            else:
                return [2, 0]
        return False

    def who_won(self):
        auxTable = self.tabela
        for i in range(self.size):
            for j in range(self.size):
                if auxTable[i][j] == "O":
                    auxTable[i][j] = 1
                elif auxTable[i][j] == "X":
                    auxTable[i][j] = -1
                else:
                    auxTable[i][j] = 0
        # Linha
        for i in range(self.size):
            if (auxTable[i][0] + auxTable[i][1] + auxTable[i][2]) == 3:
                return 3
            elif (auxTable[i][0] + auxTable[i][1] + auxTable[i][2]) == -3:
                return -3

        # Coluna
        for i in range(self.size):
            if (auxTable[0][i] + auxTable[1][i] + auxTable[2][i]) == 3:
                return 3
            elif (auxTable[0][i] + auxTable[1][i] + auxTable[2][i]) == -3:
                return -3

        # Diagonal Principal
        if (auxTable[0][0] + auxTable[1][1] + auxTable[2][2]) == 3:
            return 3
        elif (auxTable[0][0] + auxTable[1][1] + auxTable[2][2]) == -3:
            return -3

        # Diagonal Secundaria
        if (auxTable[0][2] + auxTable[1][1] + auxTable[2][0]) == 3:
            return 3
        elif (auxTable[0][2] + auxTable[1][1] + auxTable[2][0]) == -3:
            return -3

        return 0

# returned false means odd,but returned true means even


def odd_or_even(number):
    if (number % 2 == 0):
        return True
    else:
        return False

# a = [["O", "", ""], ["", "", ""], ["", "", ""]]
# auxBoard = Board(a)
# auxBoard.where_i_should(1)
