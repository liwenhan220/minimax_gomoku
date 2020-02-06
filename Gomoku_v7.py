import math
import copy
import numpy as np

class Gomoku:
    def __init__(self):
        self.size = 15
        self.win = 5
        self.stack = 8
        self.t = 0
        self.b = [['.' for _ in range(self.size)] for _ in range(self.size)]
        
    def set(self, nb, nt):
        self.b = copy.deepcopy(nb)
        self.t = nt
        
    def reset(self):
        self.t = 0
        self.b = [['.' for _ in range(self.size)] for _ in range(self.size)]

    def check_draw(self):
        for i in self.b:
            for ii in i:
                if ii == '.':
                    return False
        return True
    

    def check_win(self, x, y):
        if self.check_draw():
            return True, True
        if self.t == 1:
            b_succ = any([self.backward1(x,y,0)+self.forward1(x,y,0)>self.win,
                          self.backward2(x,y,0)+self.forward2(x,y,0)>self.win,
                          self.backward3(x,y,0)+self.forward3(x,y,0)>self.win,
                          self.backward4(x,y,0)+self.forward4(x,y,0)>self.win])
            return b_succ, False
        else:
            w_succ = any([self.backward1(x,y,1)+self.forward1(x,y,1)>self.win,
                          self.backward2(x,y,1)+self.forward2(x,y,1)>self.win,
                          self.backward3(x,y,1)+self.forward3(x,y,1)>self.win,
                          self.backward4(x,y,1)+self.forward4(x,y,1)>self.win])
        return False, w_succ
    
    def backward1(self, x, y, t):
        if t == 0:
            counter = 0
            for i in range(5):
                if x-i < 0 or y-i < 0 or self.b[x-i][y-i] != 'o':
                    break
                
                counter += 1
            return counter
        else:
            counter = 0
            for i in range(5):
                if x-i < 0 or y-i < 0 or self.b[x-i][y-i] != 'x':
                    break
                
                counter += 1
            return counter
            
    # Horizontal backwards
    def backward2(self, x, y, t):
        if t == 0:
            counter = 0
            for i in range(5):
                if x-i < 0 or self.b[x-i][y] != 'o':
                    break
                
                counter += 1
            return counter
        else:
            counter = 0
            for i in range(5):
                if x-i < 0 or self.b[x-i][y] != 'x':
                    break
                
                counter += 1
            return counter
        
    # vertical backwards
    def backward3(self, x, y, t):
        if t == 0:
            counter = 0
            for i in range(5):
                if y-i < 0 or self.b[x][y-i] != 'o':
                    break
                
                counter += 1
            return counter
        else:
            counter = 0
            for i in range(5):
                if y-i < 0 or self.b[x][y-i] != 'x':
                    break
                
                counter += 1
            return counter

    #
    def backward4(self, x, y, t):
        if t == 0:
            counter = 0
            for i in range(5):
                if x-i < 0 or y+i >= len(self.b) or self.b[x-i][y+i] != 'o':
                    break
                
                counter += 1
            return counter
        else:
            counter = 0
            for i in range(5):
                if x-i < 0 or y+i >= len(self.b) or self.b[x-i][y+i] != 'x':
                    break
                
                counter += 1
            return counter

    def forward1(self, x, y, t):
        if t == 0:
            counter = 0
            for i in range(5):
                if x+i >= len(self.b) or y+i >= len(self.b) or self.b[x+i][y+i] != 'o':
                    break
                
                counter += 1
            return counter
        else:
            counter = 0
            for i in range(5):
                if x+i >= len(self.b) or y+i >= len(self.b) or self.b[x+i][y+i] != 'x':
                    break
                
                counter += 1
            return counter

    def forward2(self, x, y, t):
        if t == 0:
            counter = 0
            for i in range(5):
                if x+i >= len(self.b) or self.b[x+i][y] != 'o':
                    break
                
                counter += 1
            return counter
        else:
            counter = 0
            for i in range(5):
                if x+i >= len(self.b) or self.b[x+i][y] != 'x':
                    break
                
                counter += 1
            return counter
        

    def forward3(self, x, y, t):
        if t == 0:
            counter = 0
            for i in range(5):
                if y+i >= len(self.b) or self.b[x][y+i] != 'o':
                    break
                
                counter += 1
            return counter
        else:
            counter = 0
            for i in range(5):
                if y+i >= len(self.b) or self.b[x][y+i] != 'x':
                    break
                
                counter += 1
            return counter

    def forward4(self, x, y, t):
        if t == 0:
            counter = 0
            for i in range(5):
                if x+i >= len(self.b) or y-i < 0 or self.b[x+i][y-i] != 'o':
                    break
                
                counter += 1
            return counter
        else:
            counter = 0
            for i in range(5):
                if x+i >= len(self.b) or y-i < 0 or self.b[x+i][y-i] != 'x':
                    break
                
                counter += 1
            return counter
        
    def render(self):
        for i in self.b:            
            print(*i)
        for _ in range(5):
            print('')

    def step(self, x, y):
        if self.b[x][y] != '.':
            return self.check_win(x,y)        
        if self.t == 0:
            self.b[x][y] = 'o'
            self.t = 1
            
        else:
            self.b[x][y] = 'x'
            self.t = 0
        return self.check_win(x,y)
    
    def ai_step(self, n):
        x = math.floor(n/self.size)
        y = n % self.size
        if self.b[x][y] != '.':
            return self.check_win(x,y)        
        if self.t == 0:
            self.b[x][y] = 'o'
            self.t = 1
            
        else:
            self.b[x][y] = 'x'
            self.t = 0
        return self.check_win(x,y)

    def justify(self,ls):
        ls = list(ls)
        for x in range(len(self.b)):
            for y in range(len(self.b[x])):
                if self.b[x][y] != '.':
                    ls[x*self.size+y] = False
        return ls
    
##env = Gomoku()
##env.reset()
##bw = False
##ww = False
##env.render()
##while not (bw or ww):
##    x = int(input('x: '))
##    y = int(input('y: '))
##    bw, ww = env.step(x,y)
##    if bw and ww:
##        print('draw')
##    elif bw:
##        print('bw!')
##    elif ww:
##        print('ww!')
##    env.render()
