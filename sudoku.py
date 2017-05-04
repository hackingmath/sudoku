'''Sudoku Solver
May 3, 2017'''

firstboard = [[4,0,5,7,0,8,0,0,0],
         [9,0,7,0,0,5,0,1,0],
         [3,0,0,4,1,0,5,2,0],
         [0,0,0,2,9,0,3,8,6],
         [0,0,8,0,4,7,0,9,2],
         [1,0,2,0,3,0,0,7,0],
         [2,6,0,1,0,0,0,0,9],
         [0,5,0,6,7,0,0,0,0],
         [0,4,0,0,0,2,6,0,8]]

board = [[0,1,0,7,6,0,9,0,4],
         [0,0,0,1,0,0,0,7,0],
         [0,8,0,2,5,4,0,0,0],
         [1,0,5,0,0,0,2,0,0],
         [0,6,0,0,0,0,0,4,0],
         [0,0,7,0,0,0,3,0,9],
         [0,0,0,4,8,2,0,9,0],
         [0,9,0,0,0,6,0,0,0],
         [5,0,6,0,3,7,0,0,0]]

numbers = [x for x in range(1,10)]

class Section(object):
    '''The 3x3 sections in the board'''
    def __init__(self,board,number):
        self.rows = 3*(number//3) #the starting row
        self.cols = 3*(number%3) #the starting column
        self.nums = board[self.rows][self.cols:self.cols+3] + \
                    board[self.rows+1][self.cols:self.cols+3] + \
                    board[self.rows+2][self.cols:self.cols+3] 
        
class Row(object):
    def __init__(self,board,number):
        self.nums = board[number]

class Column(object):
    def __init__(self,board,number):
        self.nums = [board[x][number] for x in range(9)]

def printBoard(board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if c != len(board[r])-1:
                print(" ",board[r][c]," ",end ='')
            else:
                print(' ',board[r][c],' ')
    print()

def crossOut(theboard,number_to_check):
    #make copy of board
    newBoard = []
    for i,row in enumerate(theboard):
        newBoard.append([])
        for j,col in enumerate(theboard[i]):
            newBoard[i].append(col)
        
    #cross out rows
    for r in range(9):
        the_row = Row(newBoard,r)
        if number_to_check in the_row.nums:
            for n in range(len(newBoard[r])):
                if newBoard[r][n] == 0:#!= number_to_check:
                    newBoard[r][n] = 'X'
    #cross out columns:
    for c in range(9):
        the_column = Column(newBoard,c)
        if number_to_check in the_column.nums:
            for n in range(len(newBoard)):
                if newBoard[n][c] == 0:# != number_to_check:
                    newBoard[n][c] = 'X'

    return newBoard

def checkBoard(board,number_to_check):
    '''Checks rows, then cols'''
    board2 = crossOut(board,number_to_check)
    #check rows for single 0
    for r,row in enumerate(board2):
        if number_to_check not in row and row.count(0) == 1:
            #find which column the 0 is in
            col = row.index(0)
            board[r][col] = number_to_check
            checkBoard(board,number_to_check)
            break

    for j in range(len(board2[0])):
        the_col = Column(board2,j).nums
        if number_to_check not in the_col and the_col.count(0) == 1:
            #find which row the 0 is in
            row = the_col.index(0)
            board[row][j] = number_to_check
            checkBoard(board,number_to_check)
            break

    for i in range(9):
        section = Section(board2,i).nums
        if number_to_check not in section and section.count(0) == 1:
            index = section.index(0)
            r = 3*(i//3) + index//3
            c = 3*(i%3) + index % 3
            board[r][c] = number_to_check
            break
        
    #printBoard(board2)
    #return board2
for y in range(20):
    for x in numbers:
        checkBoard(board,x)
#checkBoard(board,1)
#print(board2)
printBoard(board)

    



