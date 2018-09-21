import IO, IsValid

print "Welcome to the sudoku solver. I'm going to give you an empty sudoku board in the file board.txt. Replace the dots with the numbers in your board."
IO.initBoard()
initMessage = 'Type "done" when you\'ve finished editing the text file. Type "new" to get a fresh board.: '
invalidMessage = "This board is not a valid sudoku. Either a row, column or cell has a duplicate value"
poorFormatMessage = "You have mucked up the formatting of the board. Please fix it, or type new and start over."

goodInput = False
while goodInput == False:
    response = raw_input(initMessage)
    if response == "new":
        IO.initBoard()
    
    elif response == "done":
        board = IO.readBoard()
        if not IO.isWellFormatted(board):
            print poorFormatMessage
        elif not IsValid.isValidSudoku(board):
            print invalidMessage
        
        else:
            goodInput = True
