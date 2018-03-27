from var_dump import var_dump
import board

class Node:
    node = [None]
    weight = None
    lineMarked = None
    colmMarked = None
    nextNode = [node]

    def __init__(self, board, lineMarked, colmMarked):
        self.board = board
        self.lineMarked = lineMarked
        self.colmMarked = colmMarked
        self.weight = board.how_many_times_i_can_lose()

    def make_next_node(self, myTime):
        auxList = list()
        auxTable = self.board.getTable()

        for i in range(3):
            for j in range(3):
                if (auxTable[i][j] == ""):
                    if (myTime):
                        auxTable[i][j] = "X"
                    else:
                        auxTable[i][j] = "0"
                    auxBoard = Board()
                    auxBoard.setTable(auxTable)
                    auxNode = Node(auxBoard, i, j)
                    auxList.append(auxNode)
                    auxTable[i][j] == ""
        self.nextNode = auxList

auxBoard = Board([["O", "", ""], ["", "", ""], ["", "", ""]])
teste = Node( auxBoard , None, None  )