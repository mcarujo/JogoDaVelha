# Classe Jogo para orquestrar a classe Board

from board import *


class Game:
    def my_time(self, table):
        board_local = Board()
        board_local.setTable(table)
        #result = board_local.where_win()
        weight, col, lin = board_local.where_i_should()
          # if( type(result) == list):
          #    return result
          # else:
        return [weight, col, lin]
