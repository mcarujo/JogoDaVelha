from var_dump import var_dump
import copy
from board import Board


class Node:
    node = [None]
    weight = None
    lineMarked = None
    colmMarked = None
    nextNode = list

    def __init__(self, table, lineMarked, colmMarked):
        auxBoard = Board(table)
        auxBoard.setTable(table)
        self.node = auxBoard
        self.lineMarked = lineMarked
        self.colmMarked = colmMarked
        self.weight = self.node.how_many_times_i_can_lose()

    def make_next_node(self, myTime):
        auxList = []
        auxTable = copy.deepcopy(self.node.tabela[:])
        for i in range(3):
            for j in range(3):
                if (auxTable[i][j] == None):
                    if (myTime):
                        auxTable[i][j] = "X"
                    else:
                        auxTable[i][j] = "O"
                    auxTable2 = copy.deepcopy(auxTable[:])
                    # auxBoard.setTable(auxTable)
                    auxNode = Node(auxTable2, i, j)
                    auxList.append(auxNode)
                    auxTable[i][j] = None
        self.nextNode = auxList
