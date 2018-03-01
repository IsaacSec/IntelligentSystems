import operator
import math
import copy

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

op = []
close = []
initial = [2, 8, 3, 1, 6, 4, 7, None, 5]
goal = [1, 2, 3, 8, None, 4, 7, 6, 5]

# --------------------- State Class ------------------------

class State:
    parent = None
    board = []
    index = None
    weight = 0
    depth = 0

    def __init__(self, p, b, i, d):
        self.parent = p
        self.board = b
        self.index = i
        self.depth = d
        self.weight = State.get_state_weight(b,d)

    def to_string(self):
        i = 0
        text = "+-------+"

        if self.board is None:
            text = "[]"
            return text

        for s in self.board:
            if i % 3 == 0:
                text += "\n| "
            if s is not None:
                text += str(s) + " "
            else:
                text += "/ "
            if i % 3 == 2:
                text += "|"
            i = i + 1

        text += "\n+-------+"

        return text
    
    @staticmethod
    def get_state_weight(board, depth):
        weight = depth

        for i in range(1,9):
            bi = board.index(i) 
            gi = goal.index(i)
            # Calculate the Manhattan distance
            man_dis = abs(bi % 3 - gi % 3) + abs(bi // 3 - gi // 3)
            
            weight = weight + man_dis
            
        return weight

    def equals(self, other_state):
        return self.board == other_state.board

    def clone(self):
        return State(self, copy.copy(self.board), copy.copy(self.index), copy.copy(self.depth))

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

    def print_backtrace(self):
        
        current = self

        while current is not None:
            print(current.to_string())
            
            if current.parent is not None:
                print("    | ")
                print("    v ")

            current = current.parent


# -------- Independent Functions ---------------

# Swap values of two positions in an array
def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr

# -------- Global Variable dependent functions -----------

def search():
    total_moves = 0
    while len(op) > 0:

        si = op.pop(0)

        if si.board == goal:

            print("\nNumber of moves: "+str(total_moves)+"\n")
            si.print_backtrace()
            break

        else:
            close.append(si)
            moves = gen_moves(si)
            add_to_open(moves)
            heuristic()

        total_moves = total_moves + 1

# Generates a list with all the possible resulting states given a parent state

def gen_moves (node):
    moves = []

    up = node.clone()
    down = node.clone()
    left = node.clone()
    right = node.clone()
    
    up.move(UP)
    down.move(DOWN)
    left.move(LEFT)
    right.move(RIGHT)

    moves.append(up)
    moves.append(down)
    moves.append(left)
    moves.append(right)
    
    return moves

# Adds every element in li to the Open list skipping states with None boards

def add_to_open(li):
    while len(li) > 0:
        node = li.pop()
        
        if node.board is not None:
            
            if not in_close(node) and not in_open(node):
                op.append(node)

# Checks if the node/State exists in the Close list

def in_close(node):
    index = 0
    limit = len(close)
    
    while index < limit:
        temp = close[index]
        if node.equals(temp):
            return True
        index = index + 1
    
    return False

# Checks if the node/State exists in the Close list

def in_open(node):
    index = 0
    limit = len(op)
    
    while index < limit:
        temp = op[index]
        if node.equals(temp):
            return True
        index = index + 1
    
    return False


# Sort open by the weight
def heuristic():
    op.sort(key=operator.attrgetter('weight'))




# ---------- Implementation ---------------

s0 = State(None, initial, 7, 0)
op.append(s0)
search()