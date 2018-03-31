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
        if(self.depth >= 1):
            for x in range(len(self.root.nextNode)):
                self.root.nextNode[x].make_next_node(False)
            #Wich one is the better?
            for x in range(len(self.root.nextNode)):
                if (Weight > self.root.nextNode[x].weight):
                    Weight = self.root.nextNode[x].weight

            for x in range(len(self.root.nextNode)):
                if (Weight == self.root.nextNode[x].weight):      
                    iterator.append(x)

            for x in range(len(iterator)):



        return iterator


a = [["O", None, None], [None, None, None], [None, None, None]]
auxTree = Tree(a)
Colm = auxTree.build_min_max_with_depth()
#print(Line)
print(Colm)
#var_dump(auxTree)