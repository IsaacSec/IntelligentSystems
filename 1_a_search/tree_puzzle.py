import operator
from enum import Enum
import math
import copy

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

op = []
close = []
initial = [2, 4, 5, 7, 6, 8, 0, 1, 3]
goal = [1, 2, 3, 8, None, 4, 7, 6, 5]


class State:
    board = []
    index = None
    parent = None
    weight = 0
    depth = 0

    def __init__(self, b, i, d):
        self.board = b
        self.index = i
        self.depth = d
        self.weight = State.get_state_weight(b,d)

    def to_string(self):
        i = 0
        text = ""

        if self.board is None:
            text = "[]"
            return text

        for s in self.board:
            if i % 3 == 0:
                text += "\n"
            if s is not None:
                text += str(s) + " "
            else:
                text += "/ "
            i = i + 1

        return text
    
    @staticmethod
    def get_state_weight(board, depth):
        weight = depth

        for i in range(1,9):
            bi = board.index(i) 
            gi = goal.index(i)
            man_dis = abs(bi % 3 - gi % 3) + abs(bi // 3 - gi // 3)
            
            weight = weight + man_dis
            
        return weight

    def equals(self, other_state):
        return self.board == other_state.board

    def clone(self):
        return State(copy.copy(self.board), copy.copy(self.index), copy.copy(self.depth))

    def move(self, direction):
        if direction == UP:
            check = self.index - 3
            if 9 > check >= 0:
                self.board = swap(self.board, self.index, check)
                self.index = check
            else:
                self.board = None
        elif direction == DOWN:
            check = self.index + 3
            if 9 > check >= 0:
                self.board = swap(self.board, self.index, check)
                self.index = check
            else:
                self.board = None
        elif direction == LEFT:
            check = self.index - 1
            l1 = math.floor(self.index / 3)
            l2 = math.floor(check / 3)

            if 9 > check >= 0 and l1 == l2:
                self.board = swap(self.board, self.index, check)
                self.index = check
            else:
                self.board = None
        elif direction == RIGHT:
            check = self.index + 1
            l1 = math.floor(self.index / 3)
            l2 = math.floor(check / 3)
            if 9 > check >= 0 and l1 == l2:
                self.board = swap(self.board, self.index, check)
                self.index = check
            else:
                self.board = None
        else:
            self.board = None
        
        if self.board is not None:
            self.weight = State.get_state_weight(self.board,self.depth)
            self.depth = self.depth + 1


class Tree:
    parent = None
    data = None
    child_left = None
    child_right = None
    child_up = None
    child_down = None

    def __init__(self, p, data):
        self.parent = p
        self.data = data


#     Todo: Add methods to add new Tree to the tree, update the parent and find all nodes from so to goal





def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr


def search():
    total_moves = 0
    while len(op) > 0:
        total_moves = total_moves + 1
        si = op.pop(0)
        
        print("W: "+str(si.weight)+" D: "+str(si.depth))
        print(si.to_string())
        print("-------------------")

        if si.board == goal:
            print("Goal: ", si.to_string())
            print("Total: "+str(total_moves))
            return si
        # Make the backward along from si to s0
        else:
            close.append(si)
            children = gen_children(si)
            add_nodes(children)
            heuristic()


def gen_children (node):
    children = []

    up = node.clone()
    down = node.clone()
    left = node.clone()
    right = node.clone()
    
    up.move(UP)
    down.move(DOWN)
    left.move(LEFT)
    right.move(RIGHT)

    children.append(up)
    children.append(down)
    children.append(left)
    children.append(right)
    # print(up.to_string(), down.to_string(),left.to_string(),right.to_string())
    return children


def in_close(node):
    index = 0
    limit = len(close)
    
    while index < limit:
        temp = close[index]
        if node.equals(temp):
            return True
        index = index + 1
    
    return False

def in_open(node):
    index = 0
    limit = len(op)
    
    while index < limit:
        temp = op[index]
        if node.equals(temp):
            return True
        index = index + 1
    
    return False

def add_nodes(li):
    while len(li) > 0:
        node = li.pop()
        
        if node.board is not None:
            
            if not in_close(node) and not in_open(node):
                op.append(node)
            # else:
                # print("in close")


#             Todo: Add to tree
def get_weight(node):
    node.weight = node.depth + sum(abs(b % 3 - g % 3) + abs(b // 3 - g // 3)
                                   for b, g in ((node.board.index(i), goal.index(i)) for i in range(1, 9)))


# Sort open by the weight
def heuristic():
    op.sort(key=operator.attrgetter('weight'))


array = [2, 8, 3, 1, 6, 4, 7, None, 5]

#t1 = [1,2,3,4,5,6,7,8,9]
#t2 = [1,2,3,4,5,6,7,8,9]

#s1 = State(t1, 0)
#s2 = State(t2, 0)

#print(s1.equals(s2))


test = State(array, 7, 0)

tree = Tree(None, 0)

op.append(test)
search()
close.append(test)






# moves = all_moves(test)
# add_nodes(moves)
# test1 = moves.pop(1)
# test1 = test1.move(DOWN)
# print(test1.to_string())
# search(test)
# print(test.to_string())
# test2.move(UP)
# test2.move(LEFT)
# print(test.to_string())
# print(test2.to_string())
