import random
import numpy as np
trials  = 100000
n = 8   #weeks
p = 0.6 #prob if joe plays that week
q = 0.7 #prob if joe wins that week
matrix = np.array([[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                   [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                   [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                   [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                   [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                   [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                   [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                   [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
                   [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]])


x0 = x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = 1.0

y0 = y1 = y2 = y3 = y4 = y5 = y6 = y7 = y8 = 1.0






def joint():
    print("Joint PMF of X and Y")
    print("   y: 0      1      2      3      4      5      6      7      8")
    print("x -----------------------------------------------------------------")
    print("0 | {:.4f} ".format((matrix[0][0])/trials))
    print("1 | {:.4f} {:0.4f} ".format((matrix[1][0])/trials,(matrix[1][1])/trials))
    print("2 | {:.4f} {:0.4f} {:0.4f} ".format((matrix[2][0])/trials,(matrix[2][1])/trials,(matrix[2][2])/trials))
    print("3 | {:.4f} {:0.4f} {:0.4f} {:0.4f} ".format((matrix[3][0])/trials,(matrix[3][1])/trials,(matrix[3][2])/trials,(matrix[3][3])/trials))
    print("4 | {:.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format((matrix[4][0])/trials,(matrix[4][1])/trials,(matrix[4][2])/trials,(matrix[4][3])/trials,(matrix[4][4])/trials))
    print("5 | {:.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format((matrix[5][0])/trials,(matrix[5][1])/trials,(matrix[5][2])/trials,(matrix[5][3])/trials,(matrix[5][4])/trials,(matrix[5][5])/trials))
    print("6 | {:.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format((matrix[6][0])/trials,(matrix[6][1])/trials,(matrix[6][2])/trials,(matrix[6][3])/trials,(matrix[6][4])/trials,(matrix[6][5])/trials,(matrix[6][6])/trials))
    print("7 | {:.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format((matrix[7][0])/trials,(matrix[7][1])/trials,(matrix[7][2])/trials,(matrix[7][3])/trials,(matrix[7][4])/trials,(matrix[7][5])/trials,(matrix[7][6])/trials,(matrix[7][7])/trials))
    print("8 | {:.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format((matrix[8][0])/trials,(matrix[8][1])/trials,(matrix[8][2])/trials,(matrix[8][3])/trials,(matrix[8][4])/trials,(matrix[8][5])/trials,(matrix[8][6])/trials,(matrix[8][7])/trials,(matrix[8][8])/trials))

def XGivenY():

    y0 = (matrix[0][0]+matrix[1][0]+matrix[2][0]+matrix[3][0]+matrix[4][0]+matrix[5][0]+matrix[6][0]+matrix[7][0]+matrix[8][0])/trials
    y1 = (matrix[0][1]+matrix[1][1]+matrix[2][1]+matrix[3][1]+matrix[4][1]+matrix[5][1]+matrix[6][1]+matrix[7][1]+matrix[8][1])/trials
    y2 = (matrix[0][2]+matrix[1][2]+matrix[2][2]+matrix[3][2]+matrix[4][2]+matrix[5][2]+matrix[6][2]+matrix[7][2]+matrix[8][2])/trials
    y3 = (matrix[0][3]+matrix[1][3]+matrix[2][3]+matrix[3][3]+matrix[4][3]+matrix[5][3]+matrix[6][3]+matrix[7][3]+matrix[8][3])/trials
    y4 = (matrix[0][4]+matrix[1][4]+matrix[2][4]+matrix[3][4]+matrix[4][4]+matrix[5][4]+matrix[6][4]+matrix[7][4]+matrix[8][4])/trials
    y5 = (matrix[0][5]+matrix[1][5]+matrix[2][5]+matrix[3][5]+matrix[4][5]+matrix[5][5]+matrix[6][5]+matrix[7][5]+matrix[8][5])/trials
    y6 = (matrix[0][6]+matrix[1][6]+matrix[2][6]+matrix[3][6]+matrix[4][6]+matrix[5][6]+matrix[6][6]+matrix[7][6]+matrix[8][6])/trials
    y7 = (matrix[0][7]+matrix[1][7]+matrix[2][7]+matrix[3][7]+matrix[4][7]+matrix[5][7]+matrix[6][7]+matrix[7][7]+matrix[8][7])/trials
    y8 = (matrix[0][8]+matrix[1][8]+matrix[2][8]+matrix[3][8]+matrix[4][8]+matrix[5][8]+matrix[6][8]+matrix[7][8]+matrix[8][8])/trials

    print("Conditional PMF of X given Y")
    print("   y: 0      1      2      3      4      5      6      7      8")
    print("x -----------------------------------------------------------------")
    print("0 | {:0.4f} ".format((((matrix[0][0])/trials))/y0))
    print("1 | {:0.4f} {:0.4f} ".format(((matrix[1][0])/trials)/y0,((matrix[1][1])/y1)/trials))
    print("2 | {:0.4f} {:0.4f} {:0.4f} ".format(((matrix[2][0])/trials)/y0,((matrix[2][1])/y1)/trials,((matrix[2][2])/y2)/trials))
    print("3 | {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format(((matrix[3][0])/trials)/y0,((matrix[3][1])/y1)/trials,((matrix[3][2])/y2)/trials,((matrix[3][3])/y3)/trials))
    print("4 | {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format(((matrix[4][0])/trials)/y0,((matrix[4][1])/y1)/trials,((matrix[4][2])/y2)/trials,((matrix[4][3])/y3)/trials,((matrix[4][4])/y4)/trials))
    print("5 | {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format(((matrix[5][0])/trials)/y0,((matrix[5][1])/y1)/trials,((matrix[5][2])/y2)/trials,((matrix[5][3])/y3)/trials,((matrix[5][4])/y4)/trials,((matrix[5][5])/y5)/trials))
    print("6 | {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format(((matrix[6][0])/trials)/y0,((matrix[6][1])/y1)/trials,((matrix[6][2])/y2)/trials,((matrix[6][3])/y3)/trials,((matrix[6][4])/y4)/trials,((matrix[6][5])/y5)/trials,((matrix[6][6])/y6)/trials))
    print("7 | {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format(((matrix[7][0])/trials)/y0,((matrix[7][1])/y1)/trials,((matrix[7][2])/y2)/trials,((matrix[7][3])/y3)/trials,((matrix[7][4])/y4)/trials,((matrix[7][5])/y5)/trials,((matrix[7][6])/y6)/trials,(matrix[7][7])/y7/trials))
    print("8 | {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f}".format(((matrix[8][0])/trials)/y0,((matrix[8][1])/y1)/trials,((matrix[8][2])/y2)/trials,((matrix[8][3])/y3)/trials,((matrix[8][4])/y4)/trials,((matrix[8][5])/y5)/trials,((matrix[8][6])/y6)/trials,(matrix[8][7])/y7/trials,(matrix[8][8])/y8/trials))

def YGivenX():
    x0 = (matrix[0][0]+matrix[0][1]+matrix[0][2]+matrix[0][3]+matrix[0][4]+matrix[0][5]+matrix[0][6]+matrix[0][7]+matrix[0][8])/trials
    x1 = (matrix[1][0]+matrix[1][1]+matrix[1][2]+matrix[1][3]+matrix[1][4]+matrix[1][5]+matrix[1][6]+matrix[1][7]+matrix[1][8])/trials
    x2 = (matrix[2][0]+matrix[2][1]+matrix[2][2]+matrix[2][3]+matrix[2][4]+matrix[2][5]+matrix[2][6]+matrix[2][7]+matrix[2][8])/trials
    x3 = (matrix[3][0]+matrix[3][1]+matrix[3][2]+matrix[3][3]+matrix[3][4]+matrix[3][5]+matrix[3][6]+matrix[3][7]+matrix[3][8])/trials
    x4 = (matrix[4][0]+matrix[4][1]+matrix[4][2]+matrix[4][3]+matrix[4][4]+matrix[4][5]+matrix[4][6]+matrix[4][7]+matrix[4][8])/trials
    x5 = (matrix[5][0]+matrix[5][1]+matrix[5][2]+matrix[5][3]+matrix[5][4]+matrix[5][5]+matrix[5][6]+matrix[5][7]+matrix[5][8])/trials
    x6 = (matrix[6][0]+matrix[6][1]+matrix[6][2]+matrix[6][3]+matrix[6][4]+matrix[6][5]+matrix[6][6]+matrix[6][7]+matrix[6][8])/trials
    x7 = (matrix[7][0]+matrix[7][1]+matrix[7][2]+matrix[7][3]+matrix[7][4]+matrix[7][5]+matrix[7][6]+matrix[7][7]+matrix[7][8])/trials
    x8 = (matrix[8][0]+matrix[8][1]+matrix[8][2]+matrix[8][3]+matrix[8][4]+matrix[8][5]+matrix[8][6]+matrix[8][7]+matrix[8][8])/trials
    print("Conditional PMF of Y given X")
    print("   y: 0      1      2      3      4      5      6      7      8")
    print("x -----------------------------------------------------------------")
    print("0 | {:0.4f} ".format(((matrix[0][0])/trials)/x0))
    print("1 | {:0.4f} {:0.4f} ".format(((matrix[1][0])/trials)/x1,((matrix[1][1])/x1)/trials))
    print("2 | {:0.4f} {:0.4f} {:0.4f} ".format(((matrix[2][0])/trials)/x2,((matrix[2][1])/x2)/trials,((matrix[2][2])/x2)/trials))
    print("3 | {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format(((matrix[3][0])/trials)/x3,((matrix[3][1])/x3)/trials,((matrix[3][2])/x3)/trials,((matrix[3][3])/x3)/trials))
    print("4 | {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format(((matrix[4][0])/trials)/x4,((matrix[4][1])/x4)/trials,((matrix[4][2])/x4)/trials,((matrix[4][3])/x4)/trials,((matrix[4][4])/x4)/trials))
    print("5 | {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format(((matrix[5][0])/trials)/x5,((matrix[5][1])/x5)/trials,((matrix[5][2])/x5)/trials,((matrix[5][3])/x5)/trials,((matrix[5][4])/x5)/trials,((matrix[5][5])/x5)/trials))
    print("6 | {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format(((matrix[6][0])/trials)/x6,((matrix[6][1])/x6)/trials,((matrix[6][2])/x6)/trials,((matrix[6][3])/x6)/trials,((matrix[6][4])/x6)/trials,((matrix[6][5])/x6)/trials,((matrix[6][6])/x6)/trials))
    print("7 | {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} ".format(((matrix[7][0])/trials)/x7,((matrix[7][1])/x7)/trials,((matrix[7][2])/x7)/trials,((matrix[7][3])/x7)/trials,((matrix[7][4])/x7)/trials,((matrix[7][5])/x7)/trials,((matrix[7][6])/x7)/trials,(matrix[7][7])/x7/trials))
    print("8 | {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f} {:0.4f}".format(((matrix[8][0])/trials)/x8,((matrix[8][1])/x8)/trials,((matrix[8][2])/x8)/trials,((matrix[8][3])/x8)/trials,((matrix[8][4])/x8)/trials,((matrix[8][5])/x8)/trials,((matrix[8][6])/x8)/trials,(matrix[8][7])/x8/trials,(matrix[8][8])/x8/trials))


for i in range(trials):
    x = 0 #plays
    y = 0 #wins
    for j in range(n):
        outcome = random.random() #flip a coin
        if(outcome<=p):
            x+=1 #if he plays 
            outcome = random.random() #flip another coin
            if(outcome<=q):
                y+=1 #if he wins 
    matrix[x][y]+=1 #increment the (x,y)


joint()
print
XGivenY()
print
YGivenX()