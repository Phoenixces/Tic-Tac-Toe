board = [" " for i in range(10)]
def insertLetter(letter,pos):
    board[pos] = letter
def space_free(pos):
    return board[pos] == " "  #when space free returns true
def is_board_full(board):     #space full or not
    if board.count(" ")>1:
        return False
    else:
        return True
def printBoard(board): #Function to print the board
    print("-"*12)
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3])
    print("   |   |   ")
    print("-"*12)
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6])
    print("   |   |   ")
    print("-"*12)
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9])
    print("   |   |   ")
    print("-"*12)
def IsWinner(b,l):
    return  ((b[1] == l and b[2] == l and b[3] == l) or (b[4] == l and b[5] == l and b[6] == l) or (b[7] == l and b[8] == l and b[9] == l) or (b[1] == l and b[4] == l and b[7] == l) or (b[2] == l and b[5] == l and b[8] == l) or (b[3] == l and b[6] == l and b[9] == l) or (b[1] == l and b[5] == l and b[9] == l) or (b[3] == l and b[5] == l and b[7] == l)) #All possible moves by which player can win.
def Player_move():
    run=True
    while run:
        move = input("Please select a position to enter \"x\" b/w 1 to 9 : ")
        try:
            move = int(move)
            if move>0 and move <10:
                if space_free(move):
                    run = False
                    insertLetter("x",move)
                else:
                    print("Sorry, space  occupied..:(")
            else:
                print("Please enter a no. between 1-10 : ")
        except:
            print("Please type a number..!")
def computer_move():
    possibleMoves = [x for x,letter in enumerate(board) if letter == ' ' and x!=0 ]
    move=0
    for let in ['o','x']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move
    #checking if corner move is possible
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    #checking if centre move is possible
    if 5 in possibleMoves:
        move = 5
        return move
    #checking if edge move is possible
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
def main():
    print("TIC - TAC - TOE Welcomes you..hope u will enjoy the game:))")
    printBoard(board)
    while not(is_board_full(board)): #when is_board_full function returns false
        if not(IsWinner(board,'o')): #checks when computer is not winner..computer move is: 'o'
                                     #means if IsWinner returns false for parameter 'o' and board.
            Player_move()
            printBoard(board)
        else:
            print("Sorry ,u loose..:(")
            break
        if not(IsWinner(board,'x')):
            move = computer_move()
            if move == 0: #no moves left for computer
                print("Tie game..!")#or leave this print statement empty.
            else:
                insertLetter('o' , move)
                print("computer placed an 'o' at position" , move )    
                printBoard(board)
        else: #when user win that IsWinner returns True
            print("U Win ")
            break
        
    if is_board_full(board):
        print("Tie game..!!")


while True:
    x = input("Do u want to play ..?:(y/n)")
    if x.lower() == 'y':
        board = [" " for x in range(10)]
        print("-"*12)
        main()
    elif (x.lower() == 'n'):
        break
    else:
        print("Please Enter a valid letter..!")
       
