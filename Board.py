class Board:
    tabela = [
                ["X", "X", ""], 
                ["O", "O", "X"], 
                ["", "", "X"] 
            ]
    size = 3 
    
    def clean(self):
         for i in range(self.size):
             for j in range(self.size):
                 self.tabela[i][j] = ""
    
    def print(self):
         for i in range(self.size):
                 print(self.tabela[i][0] + " | " + self.tabela[i][1] + " | " + self.tabela[i][2])
    
    def mark(self,mark,line,colm):
         self.tabela[line][colm] = mark

    def where_lose(self):
        count = 0
        tabela_local = self.tabela
        for i in range(self.size):
            for j in range(self.size):
                if tabela_local[i][j] == "X":
                    tabela_local[i][j] = 1
                else:
                    tabela_local[i][j] = -1

        for i in range(self.size):
            if (tabela_local[i][0] + tabela_local[i][1] + tabela_local[i][2]) == -3:
                count = count + 1

        for i in range(self.size):
            if (tabela_local[0][i] + tabela_local[1][i] + tabela_local[2][i]) == -3:
                count = count + 1

        if (tabela_local[0][0] + tabela_local[1][1] + tabela_local[2][2]) == -3:
            count = count + 1
        
        if (tabela_local[0][2] + tabela_local[1][1] + tabela_local[2][0]) == -3:
            count = count + 1      
        
        return count
    
     def where_i_should(self):
        Weight = -1
        Line = None
        Colm = None
        tabela_local = self.tabela
        for i in range(self.size):
            for j in range(self.size):
                if tabela_local[i][j] == "":
                   tabela_local[i][j] = "X"
                   
                   
                   
                   
                   
                   
                   tabela_local[i][j] = ""








