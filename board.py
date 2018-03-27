# Classe Board para manipulações no tabuleiro do jogo da velha
from var_dump import var_dump
import tree


class Board:
    tabela = [[None, None, None], [None, None, None], [None, None, None]]
    size = 3

    def __init__(table):
        self.setTable(table)

    def setTable(self, board):
        self.tabela = board

    def getTable(self):
        board = [
            [self.tabela[0][0], self.tabela[0][1], self.tabela[0][2]],
            [self.tabela[1][0], self.tabela[1][1], self.tabela[1][2]],
            [self.tabela[2][0], self.tabela[2][1], self.tabela[2][2]]
        ]
        return board

    def clean(self):
        for i in range(self.size):
            for j in range(self.size):
                self.tabela[i][j] = ""

    def print(self):
        for i in range(self.size):
            print(self.tabela[i][0] + " | " + self.tabela[i][1] + " | " +
                  self.tabela[i][2])

    def mark(self, mark, line, colm):
        self.tabela[line][colm] = mark

    def how_many_times_i_can_lose(self):
        count = 0
        auxTable = self.getTable()
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

    def where_i_should(self, depth):

 
        # for k in range(depth):
        #     count = 1
        # for i in range(self.size):
        #     for j in range(self.size):
        #         if (val.tabela[i][j] == ""):
        #             if (odd_or_even(k)):
        #                 val.tabela[i][j] = "0"
        #             else:
        #                 val.tabela[i][j] = "X"
        #             tree.insert(count,val)
        #             val.tabela[i][j] == ""
        #             count = count + 1
        # print('Arvore do Min Max')
        # pprint(tree)
        #     for val in array:
        # print(val)
        # for i in range(self.size):
        #     for j in range(self.size):
        #         if (auxTable.tabela[i][j] == ""):
        #             auxTable.tabela[i][j] = "X"
        #             aux = auxTable.where_i_lose()
        #             if (aux < Weight):
        #                 Weight = aux
        #                 Line = j
        #                 Colm = i
        #             auxTable.tabela[i][j] = ""
        #             auxTable.print()

        return [None, None]
        # return [Line, Colm]

    def where_i_win(self):
        auxTable = self.getTable()
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
        auxTable = self.getTable()
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
