from var_dump import var_dump
import copy
from node import Node


class Tree:
    root = [None]
    depth = 3

    def __init__(self, table,depth):
        node = Node(table, None, None)
        self.root = node
        self.depth = depth

    def build_min_max_with_depth(self):
        self.root.make_next_node(True)
        if(self.depth >= 1):
            for x in range(len(self.root.nextNode)):
                self.root.nextNode[x].make_next_node(False)

        if(self.depth >= 2):
            for x in range(len(self.root.nextNode)):
                for y in range(len(self.root.nextNode[x].nextNode)):
                    self.root.nextNode[x].nextNode[y].make_next_node(True)

        if(self.depth >= 3):
            for x in range(len(self.root.nextNode)):
                for y in range(len(self.root.nextNode[x].nextNode)):
                    for z in range(len(self.root.nextNode[x].nextNode[y].nextNode)):
                        self.root.nextNode[x].nextNode[y].nextNode[z].make_next_node(
                            False)

    def wich_one_is_the_best(self):
        auxNode = [ ]

        Weight = -100
        for val in self.root.nextNode:
            if(Weight > val.weight):
                Weight = val.weight
                auxNode = val

        if(self.depth == 1):
            for x in range(len(self.root.nextNode)):
                Weight = -100
                for val in self.root.nextNode[x].nextNode:
                    if(Weight > val.weight):
                        Weight = self.root.nextNode[x].weight
                        auxNode = self.root.nextNode[x]

        if(self.depth == 2):
            for x in range(len(self.root.nextNode)):
                for y in range(len(self.root.nextNode[x].nextNode)):
                    Weight = -100
                    for val in self.root.nextNode[x].nextNode[y].nextNode:
                        if(Weight > val.weight):
                            Weight = self.root.nextNode[x].weight
                            auxNode = self.root.nextNode[x]
                        
        if(self.depth == 3):
            for x in range(len(self.root.nextNode)):
                for y in range(len(self.root.nextNode[x].nextNode)):
                    for z in range(len(self.root.nextNode[x].nextNode[y].nextNode)):
                        Weight = -100
                        for val in self.root.nextNode[x].nextNode[y].nextNode[z].nextNode:
                            if(Weight > val.weight):
                                Weight = self.root.nextNode[x].weight
                                auxNode = self.root.nextNode[x]
        auxNode.nextNode = None
        # return auxNode

        return [auxNode.lineMarked,auxNode.colmMarked]