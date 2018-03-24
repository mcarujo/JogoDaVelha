# Classe Board para manipulações no tabuleiro do jogo da velha


class Board:
    tabela = [["X", "X", "O"], ["O", "O", "X"], ["O", "", "X"]]
    size = 3

    def setTable(self, board):
        self.tabela = board

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

    def where_i_lose(self):
        count = 0
        tabela_local = self.tabela
        for i in range(self.size):
            for j in range(self.size):
                if tabela_local[i][j] == "X":
                    tabela_local[i][j] = 1
                else:
                    tabela_local[i][j] = -1

        for i in range(self.size):
            if (tabela_local[i][0] + tabela_local[i][1] +
                    tabela_local[i][2]) == -3:
                count = count + 1

        for i in range(self.size):
            if (tabela_local[0][i] + tabela_local[1][i] +
                    tabela_local[2][i]) == -3:
                count = count + 1

        if (tabela_local[0][0] + tabela_local[1][1] +
                tabela_local[2][2]) == -3:
            count = count + 1

        if (tabela_local[0][2] + tabela_local[1][1] +
                tabela_local[2][0]) == -3:
            count = count + 1

        return count

    def where_i_should(self):
        Weight = 100
        Line = None
        Colm = None
        for i in range(self.size):
            for j in range(self.size):
                if self.tabela[i][j] == "":
                    self.tabela[i][j] = "X"
                    aux = self.where_i_lose()
                    if (aux < Weight):
                        Weight = aux
                        Line = j
                        Colm = i
                    self.tabela[i][j] = ""
        return [Weight, Line, Colm]

    def where_win(self):
        tabela_local = self.tabela
        for i in range(self.size):
            for j in range(self.size):
                if tabela_local[i][j] == "X":
                    tabela_local[i][j] = 1
                elif tabela_local[i][j] == "O":
                    tabela_local[i][j] = -1
                else:
                    tabela_local[i][j] = 0
        # Linha
        for i in range(self.size):
            if (tabela_local[i][0] + tabela_local[i][1] +
                    tabela_local[i][2]) == 2:
                if tabela_local[i][0] == 0:
                    return [i, 0]
                elif tabela_local[i][1] == 0:
                    return [i, 1]
                else:
                    return [i, 2]
        #Coluna
        for i in range(self.size):
            if (tabela_local[0][i] + tabela_local[1][i] +
                    tabela_local[2][i]) == 2:
                if tabela_local[0][i] == 0:
                    return [0, i]
                elif tabela_local[1][i] == 0:
                    return [1, i]
                else:
                    return [2, i]
        #Diagonal Principal
        if (tabela_local[0][0] + tabela_local[1][1] + tabela_local[2][2]) == 2:
            if tabela_local[0][0] == 0:
                return [0, 0]
            elif tabela_local[1][1] == 0:
                return [1, 1]
            else:
                return [2, 2]
        #Diagonal Secundaria
        if (tabela_local[0][2] + tabela_local[1][1] + tabela_local[2][0]) == 2:
            if tabela_local[0][2] == 0:
                return [0, 2]
            elif tabela_local[1][1] == 0:
                return [1, 1]
            else:
                return [2, 0]
        return False

    def where_win(self):
        tabela_local = self.tabela
        for i in range(self.size):
            for j in range(self.size):
                if tabela_local[i][j] == "X":
                    tabela_local[i][j] = 1
                elif tabela_local[i][j] == "O":
                    tabela_local[i][j] = -1
                else:
                    tabela_local[i][j] = 0
        # Linha
        for i in range(self.size):
            if (tabela_local[i][0] + tabela_local[i][1] +
                    tabela_local[i][2]) == 2:
                if tabela_local[i][0] == 0:
                    return [i, 0]
                elif tabela_local[i][1] == 0:
                    return [i, 1]
                else:
                    return [i, 2]
        #Coluna
        for i in range(self.size):
            if (tabela_local[0][i] + tabela_local[1][i] +
                    tabela_local[2][i]) == 2:
                if tabela_local[0][i] == 0:
                    return [0, i]
                elif tabela_local[1][i] == 0:
                    return [1, i]
                else:
                    return [2, i]
        #Diagonal Principal
        if (tabela_local[0][0] + tabela_local[1][1] + tabela_local[2][2]) == 2:
            if tabela_local[0][0] == 0:
                return [0, 0]
            elif tabela_local[1][1] == 0:
                return [1, 1]
            else:
                return [2, 2]
        #Diagonal Secundaria
        if (tabela_local[0][2] + tabela_local[1][1] + tabela_local[2][0]) == 2:
            if tabela_local[0][2] == 0:
                return [0, 2]
            elif tabela_local[1][1] == 0:
                return [1, 1]
            else:
                return [2, 0]
        return False
