from Gomoku_v7 import Gomoku
import numpy as np
import copy
import math
search_n = 6
block_penalty = 1 #problematic
null_reward = 0
stone_reward = 2
ini_reward = 1
SEARCH_DEPTH = 5
search_node = 15
infinity = float('inf')
edge_pts = [0,1,2,3,15,30,45,14,13,12,11,224,223,222,221,209,194,179]
edge_penalty = 2
epsilon = 0.0
score_list = {'000100':30,
              '002100':30,
              '020100':30,
              '200100':30,
              '010002':30,
              '001120':60,
              '011020':80,
              '200110':100,
              '001100':100,
              '011100':3000,
              '011010':3000,
              '010112':1500,
              '011012':1500,
              '001112':1500,
              '011112':5000,
              '211101':5000,
              '211011':5000,
              '210111':5000,
              '011110':10000000000,
              '111112':100000000000000000000000000000,
              '111110':100000000000000000000000000000}

def b1(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if x-i<0 or y-i<0 or b[x-i][y-i]=='x':
                counter -= block_penalty
                break
            if b[x-i][y-i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    else:
        counter = ini_reward
        for i in range(1, search_n):
            if x-i<0 or y-i<0 or b[x-i][y-i]=='o':
                counter -= block_penalty
                break
            if b[x-i][y-i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    return counter

def b2(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if x-i<0 or b[x-i][y]=='x':
                counter -= block_penalty
                break
            if b[x-i][y] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    else:
        counter = ini_reward
        for i in range(1, search_n):
            if x-i<0 or b[x-i][y]=='o':
                counter -= block_penalty
                break
            if b[x-i][y] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    return counter

def b3(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if y-i<0 or b[x][y-i]=='x':
                counter -= block_penalty
                break
            
            if b[x][y-i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    else:
        counter = ini_reward
        for i in range(1, search_n):
            if y-i<0 or b[x][y-i]=='o':
                counter -= block_penalty
                break
            if b[x][y-i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    return counter

def b4(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if x+i>=len(b) or y-i<0 or b[x+i][y-i]=='x':
                counter -= block_penalty
                break
            if b[x+i][y-i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    else:
        counter = ini_reward
        for i in range(1, search_n):
            if x+i>=len(b) or y-i<0 or b[x+i][y-i]=='o':
                counter -= block_penalty
                break
            if b[x+i][y-i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    return counter

def f1(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if x+i>=len(b) or y+i>=len(b) or b[x+i][y+i]=='x':
                counter -= block_penalty
                break
            if b[x+i][y+i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    else:
        counter = ini_reward
        for i in range(1, search_n):
            if x+i>=len(b) or y+i>=len(b) or b[x+i][y+i]=='o':
                counter -= block_penalty
                break
            if b[x+i][y+i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    return counter

def f2(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if x+i>=len(b) or b[x+i][y]=='x':
                counter -= block_penalty
                break
            if b[x+i][y] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    else:
        counter = ini_reward
        for i in range(1, search_n):
            if x+i>=len(b) or b[x+i][y]=='o':
                counter -= block_penalty
                break
            if b[x+i][y] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    return counter

def f3(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if y+i>=len(b) or b[x][y+i]=='x':
                counter -= block_penalty
                break
            if b[x][y+i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward

    else:
        counter = ini_reward
        for i in range(1, search_n):
            if y+i>=len(b) or b[x][y+i]=='o':
                counter -= block_penalty
                break
            if b[x][y+i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    return counter

def f4(x,y,b,t):
    if t == 0:
        counter = ini_reward
        for i in range(1, search_n):
            if x-i<0 or y+i>=len(b) or b[x-i][y+i]=='x':
                counter -= block_penalty
                break

            if b[x-i][y+i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    else:
        counter = ini_reward
        for i in range(1, search_n):
            if x-i<0 or y+i>=len(b) or b[x-i][y+i]=='o':
                counter -= block_penalty
                break

            if b[x-i][y+i] == '.':
                counter += null_reward
                break
            else:
                counter += stone_reward
    return counter
    
def evaluate_pol(game, t):
    values = [0 for _ in range(game.size**2)]
    if t == 0:
        ot = 1
    else:
        ot = 0
    rb = copy.deepcopy(game.b)
    rt = copy.copy(game.t)
    
    for x in range(game.size):
        for y in range(game.size):
            if rb[x][y] != '.':
                values[x*game.size+y] = float('-inf')
            else:    
                value = ([b1(x,y,rb,t)+f1(x,y,rb,t), b2(x,y,rb,t)+f2(x,y,rb,t), b3(x,y,rb,t)+f3(x,y,rb,t), b4(x,y,rb,t)+f4(x,y,rb,t)])
                threat = ([b1(x,y,rb,ot)+f1(x,y,rb,ot), b2(x,y,rb,ot)+f2(x,y,rb,ot), b3(x,y,rb,ot)+f3(x,y,rb,ot), b4(x,y,rb,ot)+f4(x,y,rb,ot)])
                value = max(value)
                threat = max(threat)                     
                values[x*game.size+y] = int(value) + int(threat)
                
    for i in edge_pts:
        values[i] -= edge_penalty
    return values
    
def evaluate(game, t):
    global score_list
    b_score = 0
    w_score = 0
    for x in range(game.size):
        for y in range(game.size):
            try:
                state = ''
                os = ''
                for i in range(6):
                    if game.b[x+i][y+i] == 'o':
                        state += '1'
                        os += '2'
                    elif game.b[x+i][y+i] == 'x':
                        state += '2'
                        os += '1'
                    else:
                        state += '0'
                        os += '0'
                if state in score_list:
                    b_score += score_list[state]
                if os in score_list:
                    w_score += score_list[os]
                if state[::-1] in score_list:
                    b_score += score_list[state[::-1]]
                if os[::-1] in score_list:
                    w_score += score_list[os[::-1]]
            except:
                pass
            
            try:
                state = ''
                os = ''
                for i in range(6):
                    if y-i < 0:
                        raise NameError('negative index')
                    if game.b[x+i][y-i] == 'o':
                        state += '1'
                        os += '2'
                    elif game.b[x+i][y-i] == 'x':
                        state += '2'
                        os += '1'
                    else:
                        state += '0'
                        os += '0'
                if state in score_list:
                    b_score += score_list[state]
                if os in score_list:
                    w_score += score_list[os]
                if state[::-1] in score_list:
                    b_score += score_list[state[::-1]]
                if os[::-1] in score_list:
                    w_score += score_list[os[::-1]]
            except:
                pass
            
            try:
                state = ''
                os = ''
                for i in range(6):
                    if game.b[x+i][y] == 'o':
                        state += '1'
                        os += '2'
                    elif game.b[x+i][y] == 'x':
                        state += '2'
                        os += '1'
                    else:
                        state += '0'
                        os += '0'
                if state in score_list:
                    b_score += score_list[state]
                if os in score_list:
                    w_score += score_list[os]
                if state[::-1] in score_list:
                    b_score += score_list[state[::-1]]
                if os[::-1] in score_list:
                    w_score += score_list[os[::-1]]
            except:
                pass
            
            try:
                state = ''
                os = ''
                for i in range(6):
                    if game.b[x][y+i] == 'o':
                        state += '1'
                        os += '2'
                    elif game.b[x][y+i] == 'x':
                        state += '2'
                        os += '1'
                    else:
                        state += '0'
                        os += '0'
                if state in score_list:
                    b_score += score_list[state]
                if os in score_list:
                    w_score += score_list[os]
                if state[::-1] in score_list:
                    b_score += score_list[state[::-1]]
                if os[::-1] in score_list:
                    w_score += score_list[os[::-1]]
            except:
                pass
    if t == 0:
        return b_score - w_score
    else:
        return w_score - b_score
                    
    
def alphaBeta(game, depth, alpha, beta, maximizing, terminal, side):
    if depth == 0 or terminal:
        return 0, evaluate(game, side)

    rb = copy.deepcopy(game.b)
    rt = copy.copy(game.t)
    
    if maximizing:
        
        maxEval = -infinity
        new_game = Gomoku()
        values = list(evaluate_pol(game, game.t))
                
        best_move = np.argmax(values)
        for _ in range(search_node):
            new_game.set(rb, rt)
            if np.random.random() > epsilon:
                action = np.argmax(values)
            else:
                action = np.argmax(new_game.justify(np.random.uniform(high=1,low=-1,size=(game.size**2))))
            values[action] = False
            bw, ww = new_game.ai_step(action)
            done = bw or ww
            _, evaluation = alphaBeta(new_game, depth-1, alpha, beta, False, done, side)
            if evaluation > maxEval:
                best_move = action
                maxEval = evaluation
            alpha = max([alpha, evaluation])
            if beta <= alpha:
                break
        return best_move, maxEval

    else:
        minEval = infinity
        new_game = Gomoku()
        values = list(evaluate_pol(game, game.t))
                
        best_move = np.argmax(values)
        
        for _ in range(search_node):
            new_game.set(rb, rt)
            if np.random.random() > epsilon:
                action = np.argmax(values)
            else:
                action = np.argmax(new_game.justify(np.random.uniform(high=1,low=-1,size=(game.size**2))))
            values[action] = False
            bw, ww = new_game.ai_step(action)
            done = bw or ww
            _, evaluation = alphaBeta(new_game, depth-1, alpha, beta, True, done, side)
            if evaluation < minEval:
                best_move = action
                minEval = evaluation
            beta = min([beta, evaluation])
            if beta <= alpha:
                break
        return best_move, minEval

