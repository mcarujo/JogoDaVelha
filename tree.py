from var_dump import var_dump
from node import Node

class Tree:
    root = [None]
    depth = 1

    def __init__(self, table):
        node = Node(table,None,None)
        self.root = node

    def build_min_max_with_depth(self):
        self.root.make_next_node(True)
        Line = None
        Colm = None
        Weight = 100
        iterator = []
        iterator2 = []
        if(self.depth >= 1):
            for x in range(len(self.root.nextNode)):
                if (Weight > self.root.nextNode[x].weight):
                    Weight = self.root.nextNode[x].weight

            for x in range(len(self.root.nextNode)):
                if (Weight == self.root.nextNode[x].weight):      
                    iterator.append(x)

            for x in range(len(iterator)):
                self.root.nextNode[iterator[x]].make_next_node(False)
                Weight = 100
                for y in range(len(self.root.nextNode[iterator[x]].nextNode)):
                    if (Weight > self.root.nextNode[iterator[x]].nextNode[y].weight):
                        Weight = self.root.nextNode[iterator[x]].nextNode[y].weight
                for y in range(len(self.root.nextNode[iterator[x]].nextNode)):
                    if (Weight == self.root.nextNode[iterator[x]].nextNode[y].weight):      
                        iterator2= [ iterator[x], Weight ]               


        var_dump(iterator2)  
                #var_dump(self.root.nextNode[iterator[x]])






        return iterator2


a = [["O", None, None], [None, None, None], [None, None, None]]
auxTree = Tree(a)
Colm = auxTree.build_min_max_with_depth()
#print(Line)
print(Colm)
#var_dump(auxTree)