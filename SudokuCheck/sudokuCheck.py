""" Hi, here's your problem today. 
(You've reached the end of the 
problems for now - in the meanwhile,
here is a random question. And visit 
CoderPro for more practice!) 
This problem was recently asked by Facebook:

A Sudoku board is a 9x9 grid, 
where each row, column and each 
3x3 subbox contains the number from 1-9. 
Here's an example of a Sudoku board.

refer:
1. https://dev.to/aspittel/how-i-finally-wrote-a-sudoku-solver-177g
2. http://norvig.com/sudoku.html
3. ...

-------------
|534|678|912|
|672|195|348|
|198|342|567|
|------------
|859|761|423|
|426|853|791|
|713|924|856|
|------------
|961|537|284|
|287|419|635|
|345|286|179|
|------------

Given a 9x9 board, determine if it is 
a valid Sudoku board. The board may be 
partially filled, where an empty cell will 
be represented by the space character ' '.
 """

def validate_sudoku(board):
    row = len(board)
    ''' check num of row '''
    if row is not 9:
        return False
    ''' check num of column '''
    for column in board:
        if len(column) is not 9:
            return False
        ''' check horizontally '''
        table = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, ' ':0}
        for i in range (0,9):
            # print(column[i])
            table[column[i]] += 1
            ''' check no duplicate '''
            if table[column[i]] == 2:
                return False
            # '''print table '''
            # if i == row-1:
            #     print(table)
    if check_col_val(board) == False: return False # check vertically
    if check_subbox(board) == False: return False # check all the 3x3 subbox
    return True

def check_col_val(board): 
    ''' check vertically '''
    for index in range(0,9):
        table = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, ' ':0}
        for col in board:
            ''' col val read & add to table '''
            table[col[index]] += 1
            ''' check no duplicate '''
            if table[col[index]] == 2:
                if col[index] != ' ':
                    return False
        # print(table) #
    return True

def check_subbox(board):
    ''' assume 9row & 9column board was checked '''
    # temp = [] #
    def check_3x3(pre_row,row_buff,pre_col,col_buff):
        table = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, ' ':0}
        for row in range (pre_row,row_buff):
            for col in range (pre_col,col_buff):
                # temp.append(board[row][col]) #
                table[board[row][col]] += 1 # add to table
                if table[board[row][col]] == 2: # check table
                    if board[row][col] != ' ': # check except ' '
                        return False
        return table

    subbox = 0
    count = 1
    row_buff = 3
    pre_row = 0
    col_buff = 3
    pre_col = 0
    table = True
    while subbox <= 8: # 0~8 (9)
        ''' check result '''
        if table == False: 
            return False

        ''' loop increment '''
        subbox += 1 

        ''' reset count '''
        if count >= 4: 
            count = 1
            pre_col = col_buff
            col_buff = 3

        ''' all (col 1,2,3) 3x3 subbox is 3 in total checked '''
        if subbox <= 3: 
            table = check_3x3(pre_row,row_buff,pre_col,col_buff)
            count += 1
            pre_col = col_buff
            col_buff = 3*count
            # print(subbox) #
            # print(temp) #
            # print(table) #

        ''' all (col 4,5,6) 3x3 subbox is 3 in total checked '''
        if subbox >= 4 and subbox <= 6:
            pre_row = 3
            row_buff = 6
            table = check_3x3(pre_row,row_buff,pre_col,col_buff)
            count += 1
            pre_col = col_buff
            col_buff = 3*count
            # print(subbox) #
            # print(temp) #
            # print(table) #

        ''' all (col 7,8,9) 3x3 subbox is 3 in total checked '''
        if subbox >= 7 and subbox <= 9:
            pre_row = 6
            row_buff = 9
            table = check_3x3(pre_row,row_buff,pre_col,col_buff)
            count += 1
            pre_col = col_buff
            col_buff = 3*count
            # print(subbox) #
            # print(temp) #
            # print(table) #
    return True

board = [
    [5, ' ', 4, 6, 7, 8, 9, 1, 2],
    [6, ' ', 2, 1, 9, 5, 3, 4, 8],
    [1,   9, 8, 3, 4, 2, 5, 6, 7],
    [8,   5, 9, 7, 6, 1, 4, 2, 3],
    [4,   2, 6, 8, 5, 3, 7, 9, 1],
    [7,   1, 3, 9, 2, 4, 8, 5, 6],
    [9,   6, 1, 5, 3, 7, 2, 8, 4],
    [2,   8, 7, 4, 1, 9, 6, 3, 5],
    [3,   4, 5, 2, 8, 6, 1, 7, 9],
]

print(validate_sudoku(board))
# True

'''
concludes: 
    i dk what the fxxk is sudoku never play it & understand it:
    from observation assume 1~9 should not duplicate in:
    each row, each column, each subbox & 9x9 array. I think...

    huh...:
        1.how about many ' ' in broad.
        2.i have not check it.
        3.but i think other function was check for 1~9 row&col.
        4.so its fine.....? I think. 
    hmm...:
        1.sum a row element = 1+2+...+9 = 45
        2.sum a col element = 1+2+...+9 = 45
        3.sum a subbox element = 45 too
        4.find missing element = result - 45  
'''
# print(check_col_val(board))
'''
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
{1: 1, 2: 1, 3: 0, 4: 1, 5: 1, 6: 1, 7: 0, 8: 1, 9: 1, ' ': 2}
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
True
'''
# print(check_subbox(board))
'''
1
[5, ' ', 4, 6, ' ', 2, 1, 9, 8]
{1: 1, 2: 1, 3: 0, 4: 1, 5: 1, 6: 1, 7: 0, 8: 1, 9: 1, ' ': 2}
2
[5, ' ', 4, 6, ' ', 2, 1, 9, 8, 6, 7, 8, 1, 9, 5, 3, 4, 2]
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
3
[5, ' ', 4, 6, ' ', 2, 1, 9, 8, 6, 7, 8, 1, 9, 5, 3, 4, 2, 9, 1, 2, 3, 4, 8, 5, 6, 7]
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
4
[5, ' ', 4, 6, ' ', 2, 1, 9, 8, 6, 7, 8, 1, 9, 5, 3, 4, 2, 9, 1, 2, 3, 4, 8, 5, 6, 7]
{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, ' ': 0}
5
[5, ' ', 4, 6, ' ', 2, 1, 9, 8, 6, 7, 8, 1, 9, 5, 3, 4, 2, 9, 1, 2, 3, 4, 8, 5, 6, 7, 7, 6, 1, 8, 5, 3, 9, 2, 4]
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
6
[5, ' ', 4, 6, ' ', 2, 1, 9, 8, 6, 7, 8, 1, 9, 5, 3, 4, 2, 9, 1, 2, 3, 4, 8, 5, 6, 7, 7, 6, 1, 8, 5, 3, 9, 2, 4, 4, 2, 3, 7, 9, 1, 8, 5, 6]
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
7
[5, ' ', 4, 6, ' ', 2, 1, 9, 8, 6, 7, 8, 1, 9, 5, 3, 4, 2, 9, 1, 2, 3, 4, 8, 5, 6, 7, 7, 6, 1, 8, 5, 3, 9, 2, 4, 4, 2, 3, 7, 9, 1, 8, 5, 6]
{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, ' ': 0}
8
[5, ' ', 4, 6, ' ', 2, 1, 9, 8, 6, 7, 8, 1, 9, 5, 3, 4, 2, 9, 1, 2, 3, 4, 8, 5, 6, 7, 7, 6, 1, 8, 5, 3, 9, 2, 4, 4, 2, 3, 7, 9, 1, 8, 5, 6, 5, 3, 7, 4, 1, 9, 2, 8, 6]
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
9
[5, ' ', 4, 6, ' ', 2, 1, 9, 8, 6, 7, 8, 1, 9, 5, 3, 4, 2, 9, 1, 2, 3, 4, 8, 5, 6, 7, 7, 6, 1, 8, 5, 3, 9, 2, 4, 4, 2, 3, 7, 9, 1, 8, 5, 6, 5, 3, 7, 4, 1, 9, 2, 8, 6, 2, 8, 4, 6, 3, 5, 1, 7, 9]
{1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, ' ': 0}
True
'''