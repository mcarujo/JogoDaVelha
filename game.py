# Classe Jogo para orquestrar as classes 
from board import *
from tree import *


class Game:
    def my_time(self, table, level):
        board_local = Board(table)
        tabela = self.formatt_talble(table)

        if(type(board_local.where_i_win()) == list and int(level) >= 1 ):
            line, colm = board_local.where_i_win()
            return [line, colm]
        elif(type(board_local.where_i_lose()) == list and int(level) >= 2):
            line, colm = board_local.where_i_lose()
            return [line, colm]
        elif(type(board_local.jogada_1()) == list and int(level) >= 3):
            line, colm = board_local.jogada_1()
            return [line, colm]
        else:
            auxTree = Tree(tabela,0)
            auxTree.build_min_max_with_depth()
            line, colm = auxTree.wich_one_is_the_best()
            return [line, colm]

    def formatt_talble(self,table):
        tabela = table
        for x in range(3):
            for y in range(3):
                if (tabela[x][y] == ""):
                    tabela[x][y] = None
        return tabela

    def alguem_ganhou(self,table):
        tabela = self.formatt_talble(table)
        board_local = Board(table)
        
        retorno = board_local.deu_velha()
        if retorno:
            return [True, "Deu Velha"]
        retorno = board_local.who_won()
        if(retorno == 3 ):
            return [True, "Usuário Ganhou"]
        elif(retorno == -3 ):
            return [True, "CPU Ganhou"]
        else:
            return [False, "Ninguem Ganhou"]      
                    