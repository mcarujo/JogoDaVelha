# Classe Jogo para orquestrar a classe Board

from board import *


class Game:
    def my_time(self, table):
        board_local = Board()
        board_local.setTable(table)

        if(type(board_local.where_i_win()) == list):
            line, Colm = board_local.where_i_win()
            print('primeiro')
            return [line, Colm]
        elif (type(board_local.where_i_win()) == list):
            line, Colm = board_local.where_i_win()
            print('segundo')
            return [line, Colm]
        else:
            print('terceiro')
            print('board_local.tabela')
            print(board_local.tabela)
            line, Colm = board_local.where_i_should()
            return [line, Colm]
