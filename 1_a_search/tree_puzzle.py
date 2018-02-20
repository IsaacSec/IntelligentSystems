from enum import Enum
import math

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class State:
    board = []
    index = None

    def __init__(self, b, i):
        self.board = b
        self.index = i

    def to_string(self):
        i = 0
        text = ""
        
        if self.board == None :
            text = "[]"
            return text

        for s in self.board:
            if i % 3 == 0 :
                text += "\n"
            if s != None :
                text += str(s) + " "    
            else :
                text += "/"
            i = i+1
        
        return text
    
    def clone(self, b, i):
        return State(self.b, self.i)

    def move(self, direction):
        if direction == UP:
            check = self.index - 3
            if check < 9 or check >= 0:
                self.board = swap(self.board, self.index, check)
                self.index = check    
            else:
                self.board = None
        elif direction == DOWN:
            check = self.index + 3
            if check < 9 or check >= 0:
                self.board = swap(self.board, self.index, check)    
                self.index = check
            else:
                self.board = None
        elif direction == LEFT:
            check = self.index - 1
            l1 = math.floor(self.index/3)
            l2 = math.floor(check/3)

            if check < 9 and check >= 0 and l1 == l2:
                self.board = swap(self.board, self.index, check)
                self.index = check    
            else: 
                self.board = None
        elif direction == RIGHT:
            check = self.index + 1
            l1 = math.floor(self.index/3)
            l2 = math.floor(check/3)
            if check < 9 and check >= 0 and l1 == l2:
                self.board = swap(self.board, self.index, check)
                self.index = check    
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

    def __init__(self, p, pId):
        
        if p != None :
            self.parent = p
            self._id = p.id + pId

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr 


array = [1,2,3,4,5,None,7,8,9]

test = State(array,5)
print(test.to_string())
test.move(UP)
print(test.to_string())
test.move(RIGHT)
print(test.to_string())
