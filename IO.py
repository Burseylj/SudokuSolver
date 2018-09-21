##we require that the user call makeBoard, then replace the blank characters with
##the numbers given on their board

divider = "-------+-------+-------"
emptyBoard = [['.']*9]*9
legal = [str(x) for x in range(1,10)]  + ['.']


def initBoard():
    f = open('board.txt','w')
    f.write(makeBoard())
    f.close()

def readBoard():
    f = open('board.txt','r')
    formBoard = f.read()
    f.close()
    return getBoard(formBoard)

def makeBoard(board=emptyBoard):
    formBoard = ''
    for i in xrange(9):
        formBoard += makeRow(board[i])
        if i == 2 or i ==5:
            formBoard+= '\n' + divider

        if i != 8:                          #don't add new line to last row
            formBoard += '\n'
    return formBoard


def makeRow(row):
    formRow = ''
    for i in xrange(9):
        if isinstance(row[i],set):
            formRow += ' ' + '.'
        else:
            formRow += ' ' +row[i]
        if i == 2 or i ==5:
            formRow += ' |'
    return formRow

def getBoard(formBoard):
    board = [] 
    rows = formBoard.splitlines()
    for i in rows:
        if getRow(i) != []:            #skip divider rows
            board += [getRow(i)]
    return board

def getRow(formRow):
    return [s for s in formRow if s in legal]

def isWellFormatted(board):
    if len(board) != 9:
        return False
    for i in board:
        if len(i) != 9:
            return False
        for x in i:
            if x not in legal:
                return False
    return True

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
    
    assert makeRow(["5","3",".",".","7",".",".",".","."]) == " 5 3 . | . 7 . | . . ."

    assert getRow(" 8 3 . | . 7 . | . . .") == board2[0]
    assert board1 == getBoard(makeBoard(board1))
    assert board2 == getBoard(makeBoard(board2))
    assert emptyBoard == getBoard(makeBoard())
    assert isWellFormatted(board1)
    assert isWellFormatted(board2)
    assert not isWellFormatted(board1[:8])
    board3 = board2
    board3[1] = ["."]
    board4 = board1
    board4[8] = ['0']*9
    assert not isWellFormatted(board3)
    assert not isWellFormatted(board4)
    assert isWellFormatted(emptyBoard)
    print makeBoard(board1)
    print "tests pass"
