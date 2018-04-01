# Classe Jogo para orquestrar as classes 
from board import *
from tree import *


class Game:
    def my_time(self, table):

        board_local = Board(table)
        tabela = self.formatt_talble(table)

        if(type(board_local.where_i_win()) == list):
            line, Colm = board_local.where_i_win()
            print('primeiro')
            return [line, Colm]
        elif (type(board_local.where_i_lose()) == list):
            line, Colm = board_local.where_i_lose()
            print('segundo')
            return [line, Colm]
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
                    