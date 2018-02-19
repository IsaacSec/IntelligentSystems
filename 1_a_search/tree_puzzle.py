class State:
    board = []
    index = None

    def __init__(self, b, i):
        self.board = b
        self.index = i

    def to_string(self):
        i = 0
        text = ""
        
        for s in self.board:
            if i % 3 == 0 :
                text += "\n"
            if s != None :
                text += str(s) + " "    
            else :
                text += "/"
            i = i+1
        
        return text

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
