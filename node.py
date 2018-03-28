from var_dump import var_dump
from board import Board

class Node:
    node = [None]
    weight = None
    lineMarked = None
    colmMarked = None
    nextNode = [node]

    def __init__(self, table, lineMarked, colmMarked):
        auxBoard = Board(table)
        auxBoard.setTable(table)
        self.node =  auxBoard
        self.lineMarked = lineMarked
        self.colmMarked = colmMarked
        self.weight = self.node.how_many_times_i_can_lose()

    def make_next_node(self, myTime):
        auxList = []
        auxTable = self.node.getTable()
        # print(auxTable) 
        # var_dump(auxTable)
        for i in range(3):
            for j in range(3):
                               
                if (auxTable[i][j] == None):
                    
                    if (myTime):
                        auxTable[i][j] = "X"
                    else:
                        auxTable[i][j] = "O"
                    auxBoard = Board(auxTable)
                    # auxBoard.setTable(auxTable)
                    auxNode = Node(auxBoard, i, j)
                    auxList.append(auxNode)
                    auxTable[i][j] == None
        self.nextNode = auxList





a = [["O", None, None], [None, None, None], [None, None, None]]
teste = Node( a , 1, 1  )
print(teste.node.getTable())
# teste.make_next_node(True)
# var_dump(teste)