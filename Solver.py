from copy import deepcopy
import IO
import IsValid

nums = map(str,range(1,10))
#for each empty cell we maintain a list of possible values
def getState(board):

    state = deepcopy(board)

    for row in xrange(9):
        for col in xrange(9):
            if state[row][col] == '.':
                state[row][col] = set(nums)

    return state

def isSolved(state):
    for row in state:
        for cell in state:
            if cell not in nums:
                return false
    return true

def propagateStep(state):
    madeMove = False

    #update rows 
    for row in xrange(9):
        values = set([x for x in state[row] if x in nums])
        for col in xrange(9):
            if isinstance(state[row][col],set):
                state[row][col] -= values
                if (len(state[row][col]) == 1):
                    state[i][col] = state[row][col].pop()
                    madeMove = True
                elif (len(state[row][col]) == 0):
                    return False, None
    #update columns
    for col in xrange(9):
        column = IsValid.getCol(state, col)
        values = set([x for x in column if x in nums])
        for row in xrange(9):
            if isinstance(state[row][col], set):
                state[row][col] -= values
                if (len(state[row][col]) == 1):
                    state[row][col] = state[row][col].pop()
                    madeMove = True
                elif (len(state[row][col]) == 0):
                    return False, None
    #update sub boxes
    for sub in xrange(9):
        subBox = IsValid.getSubBox(state,sub)
        values = set([x for x in subBox if x in nums])
        startCol = (sub % 3)*3
        startRow = (sub / 3)*3
        for i in range(startRow, startRow+3):
            for j in range(startCol, startCol + 3):
                if isinstance(state[i][j], set):
                    state[i][j] -= values
                    if (len(state[i][j]) == 1):
                        state[i][j] = state[i][j].pop()
                        madeMove = True
                    elif (len(state[i][j]) == 0):
                        return False, None
                    
    return True, madeMove

emptyBoard = [['.']*9]*9
badBoard = [nums*9]*9
badBoard[0][1] = '.'
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
state1 = getState(board1)
propagateStep(state1)
assert [x for x in getState(board1)[8] if x in nums] == ['8', '7', '9']
assert [x for x in IsValid.getCol(getState(board1),0) if x in nums] == ['5', '6', '8', '4', '7']
assert [x for x in IsValid.getSubBox(getState(board1),4) if x in nums] == ['6', '8', '3', '2']
assert state1[4][4] == '5'
assert state1[6][5] == '7'
assert propagateStep(getState(board1))[0] == True
assert propagateStep(getState(badBoard))[0] == False
assert propagateStep(getState(board1))[1] == True
assert propagateStep(getState(emptyBoard))[1] == False
print "passed all tests"
