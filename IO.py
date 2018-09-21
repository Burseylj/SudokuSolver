##we require that the user call makeBoard, then replace the blank characters with
##the numbers given on their board

divider = "---------+---------+---------"
emptyBoard = [["."]*9]*9

def makeBoard(board=emptyBoard):
    formBoard = ''
    for i in xrange(9):
        formBoard += makeRow(board[i])
        if i == 2 or i ==5:
            formBoard+= '\n' + makeRow(divider)

        if i != 8:                          #don't add new line to last row
            formBoard += '\n'
    return formBoard


def makeRow(row):
    formRow = ''
    for i in xrange(9):
        formRow += ' ' +row[i]
        if i == 2 or i ==5:
            formRow += ' |'
    return formRow

def getBoard(formBoard):
    board = []
    rowsToRead = [0,1,2,4,5,6,8,9,10]  ##skip divider lines 
    rows = formBoard.splitlines()
    for i in rowsToRead:
        board += [getRow(rows[i])]
    return board

def getRow(formRow):
    legal = [str(x) for x in range(1,10)]  + ['.']
    return [s for s in formRow if s in legal]
        
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
assert makeRow(["5","3",".",".","7",".",".",".","."]) == " 5 3 . | . 7 . | . . ."

assert getRow(" 8 3 . | . 7 . | . . .") == board2[0]
assert board1 == getBoard(makeBoard(board1))

assert board2 == getBoard(makeBoard(board2))

print "tests pass"
