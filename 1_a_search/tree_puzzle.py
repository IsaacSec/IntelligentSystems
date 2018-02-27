from enum import Enum
import math
import copy

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

op = []
close = []
initial = [2, 4, 5, 7, 6, 8, None, 1, 3]
goal = [1, 2, 3, 4, None, 5, 6, 7, 8]


class State:
    board = []
    index = None

    def __init__(self, b, i):
        self.board = b
        self.index = i

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

    def clone(self):
        return State(copy.copy(self.board), copy.copy(self.index))

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


class Tree:
    parent = None
    _id = 0
    data = None
    child_left = None
    child_right = None
    child_up = None
    child_down = None

    def __init__(self, p, p_id):
        if p is not None:
            self.parent = p
            self._id = p.id + p_id


#     Todo: Add methods to add new Tree to the tree, update the parent and find all nodes from so to goal


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr


def search():
    while len(op) > 0:
        si = op.pop(0)
        if si.board == goal:
            print("Goal: ", si.to_string())
            return si
        # Make the backward along from si to s0
        else:
            move_list = all_moves(si)
            add_nodes(move_list)
            close.append(si.board)


def all_moves(node):
    movelist =[]
    up = node.clone()
    up.move(UP)
    down = node.clone()
    down.move(DOWN)
    left = node.clone()
    left.move(LEFT)
    right = node.clone()
    right.move(RIGHT)
    movelist.append(up)
    movelist.append(down)
    movelist.append(left)
    movelist.append(right)
    # print(up.to_string(), down.to_string(),left.to_string(),right.to_string())
    return movelist


def add_nodes(li):
    while len(li) > 0:
        node = li.pop()
        if node.board is not None:
            if node.board not in close:
                print(node.to_string())
                op.append(node)
            # else:
                # print("in close")


#             Todo: Add to tree


array = [1, 2, 3, 4, 5, 6, None, 7, 8]


test = State(array, 6)
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
