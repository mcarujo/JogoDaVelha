class Quadro:
    tabela = [
                ["", "", ""], 
                ["", "", ""], 
                ["", "", ""] 
            ]
    size = 3 
    def limpar(self):
         for i in range(self.size):
             for j in range(self.size):
                 self.tabela[i][j] = "#"
    
    def printar(self):
         for i in range(self.size):
                 print(self.tabela[i][0] + " | " + self.tabela[i][1] + " | " + self.tabela[i][2])
    
    def marcar(mark,line,colm,self):
         self.tabela[0][1] = mark
    

            



    
