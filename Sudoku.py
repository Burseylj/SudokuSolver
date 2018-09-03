def isValidSudoku(board):

    for i in range(9):
        #check rows
        if not isValidGroup(board[i]): return False
        #check columns
        if not isValidGroup(getCol(board,i)): return False           
        #check sub boxes
        if not isValidGroup(getSubBox(board,i)): return False
    return True 

def isValidGroup(group):
    elements = []
    for x in group:
        if x in elements: return False
        if (x != '.'): elements.append(x)
    return True 

def getCol(board, colIndex):
    column = []
    for rowIndex in range(9):
        column.append(board[rowIndex][colIndex])
    return column

def getSubBox(board, subBoxIndex):
    subBox = []
    startCol = (subBoxIndex % 3)*3
    startRow = (subBoxIndex / 3)*3
    for i in range(startRow, startRow+3):
        for j in range(startCol, startCol + 3):
            subBox.append(board[i][j])
    return subBox

def test():
    board1 = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    board2 = [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    print "board1 is {} and should be {}".format(isValidSudoku(board1), True)
    print "board2 is {} and should be {}".format(isValidSudoku(board2), False)
