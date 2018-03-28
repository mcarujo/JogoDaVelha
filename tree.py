from var_dump import var_dump
from node import Node

class Tree:
    root = [None]
    depth = None

    def __init__(self, table):
        node = Node(table,None,None)
        self.root = node

    # def give_me_the_full_tree(self):
# a = [["O", "", ""], ["", "", ""], ["", "", ""]]
# auxTree = Tree(a)
# auxTree.root.make_next_node(True)
# var_dump(auxTree)