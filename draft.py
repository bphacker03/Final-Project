import random as rand

game_board ={
    "A" : [".", ".", ".", "."],
    "B" : [".", ".", ".", "+"],
    "C" : ["-", ".", ".", "."],
    "D" : [".", ".", ".", "."]
}

tiles = []
P1tiles = ["B4"]
P1spaces = ["A3", "B3", "C3", "A4", "C4"]
P2tiles = ["C1"]
P2spaces = ["B2", "C2", "D2", "B1", "D1"]

def print_board(board):
    print("     A    B    C    D")
    for i in range(len(board.values())):
        print(str(i+1) + "    " + board["A"][i] + "    " +  board["B"][i] + "    " + board["C"][i] + "    " + board["D"][i])

def play(board):
    for i in range (16):
        print_board(board)
        P1tile = ""

        while P1tile not in P1spaces:
            P1tile = input("Where would you like to place a tile? ")

        if P1tile in P2spaces:
            P2spaces.remove(P1tile)
        P1spaces.remove(P1tile)
        tiles.append(P1tile)
        P1tiles.append(P1tile)

        P2tile = rand.choice(P2spaces)
        if P2tile in P1spaces:
            P1spaces.remove(P2tile)
        P2spaces.remove(P2tile)
        tiles.append(P2tile)
        P2tiles.append(P2tile)

        board[P1tile[0]][int(P1tile[1]) - 1] = "+"
        board[P2tile[0]][int(P2tile[1]) - 1] = "-"

print("Welcome to PyTurf!")
play(game_board)