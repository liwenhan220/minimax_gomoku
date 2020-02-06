from Gomoku_v7 import Gomoku
import numpy as np
import cv2
import time
import copy
from minimax_v7 import *
bw = False
ww = False
env = Gomoku()
ai_turn = int(input('black or white? (0 for white and 1 for black)'))
SELF_PLAY = False

def click(event, x, y, flags, params):
    global bw
    global ww
    if event == cv2.EVENT_LBUTTONDOWN:   
        x = int(x/(500/env.size))
        y = int(y/(500/env.size))
        bw, ww = env.step(y,x)
        env.render()
        draw_img(env.b)
            
def draw_img(board):
    
    cv2.namedWindow('game')
    cv2.setMouseCallback('game',click)
    gap = 15
    real_img = np.zeros((500,500,3))
    for x in range(int(len(real_img))):
        for y in range(int(len(real_img))):
            real_img[x][y] = (0, 255, 0)
                       
    for x1 in range(len(board)):
        for y1 in range(len(real_img)):
            real_img[int(len(real_img)/len(board)*x1)+gap][y1] = (0,0,0)
            real_img[y1][int(len(real_img)/len(board)*x1)+gap] = (0,0,0)

    for x2 in range(len(board)):
        for y2 in range(len(board)):
            if board[x2][y2] == 'o':
                cv2.circle(real_img, (int(((len(real_img)/len(board))*y2)+gap),int(((len(real_img)/len(board))*x2)+gap)), 11, (0,0,0),-1)
            if board[x2][y2] == 'x':
                cv2.circle(real_img, (int(((len(real_img)/len(board))*y2)+gap),int(((len(real_img)/len(board))*x2)+gap)), 11, (255, 255, 255),-1)
    cv2.imshow('game',real_img)
    cv2.waitKey(1)   

def main():
    PO = 70
    env.reset()
    env.render()
    global bw
    global ww
    if ai_turn == 0 or SELF_PLAY:
        env.step(int(env.size/2), int(env.size/2))
    while not (bw or ww):
        if (env.t == ai_turn or SELF_PLAY):
            print('ai is thinking...')
            cv = evaluate(env, env.t)
            action, val = alphaBeta(env, SEARCH_DEPTH, float('-inf'), float('inf'), True, False, env.t)
##            action = np.argmax(evaluate_pol(env, env.t))
            bw, ww = env.ai_step(action)
            print('future evaluation: ' + str(val))
            print('current_evaluation: ' + str(cv))
            env.render()
        else:
            draw_img(env.b)
    
        draw = bw and ww
        draw_img(env.b)
        if not draw:
            if bw:
                print('black won!')
                time.sleep(60)
            if ww:
                print('white_won!')
                time.sleep(60)
        else:
            print('draw!')
            time.sleep(60)
if __name__ == '__main__':
    main()
    
