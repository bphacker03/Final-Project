import random as rand

game_board ={ # contains the board seen by the player, tiles are + for the player and - for the AI and spaces are .
    "A" : [".", ".", ".", ".", "."],
    "B" : [".", ".", ".", ".", "+"],
    "C" : [".", ".", ".", ".", "."],
    "D" : ["-", ".", ".", ".", "."],
    "E" : [".", ".", ".", ".", "."]
}

tiles = ["B5", "D1"]
P1tiles = ["B5"]
P1spaces = ["A4", "B4", "C4", "A5", "C5"]
P2tiles = ["D1"]
P2spaces = ["C2", "D2", "E2", "C1", "E1"]
shared = [] # list of spaces that the player and AI can both place a tile in
columns = ["A", "B", "C", "D", "E"]
rows = ["1", "2", "3", "4", "5"]

def print_board(board): # uses a function from a past lab to display the board 
    print("     A    B    C    D    E")
    for i in range(len(board.values())):
        print(str(i+1) + "    " + board["A"][i] + "    " + board["B"][i] + "    " + board["C"][i] + "    " + board["D"][i] + "    " + board["E"][i])

def place_tile(p1tile, p1spaces, p1tiles, p2spaces): # adds/removes tile to/from appropriate lists and checks if tiles can be placed around it
    p1spaces.remove(p1tile)
    tiles.append(p1tile)
    p1tiles.append(p1tile)
    
    if p1tile in shared:
        shared.remove(p1tile)
        p2spaces.remove(p1tile)
    if p1tile[0] != columns[0] and p1tile[1] != rows[0]:
        tl = columns[columns.index(p1tile[0])-1]+rows[rows.index(p1tile[1])-1]
        if tl not in tiles and tl not in p1spaces:
            p1spaces.append(tl)    
    if p1tile[1] != rows[0]:
        tm = p1tile[0]+rows[rows.index(p1tile[1])-1]
        if tm not in tiles and tm not in p1spaces:
            p1spaces.append(tm)
    if p1tile[0] != columns[-1] and p1tile[1] != rows[0]:
        tr = columns[columns.index(p1tile[0])+1]+rows[rows.index(p1tile[1])-1]
        if tr not in tiles and tr not in p1spaces:
            p1spaces.append(tr)
    if p1tile[0] != columns[0]:
        l = columns[columns.index(p1tile[0])-1]+p1tile[1]
        if l not in tiles and l not in p1spaces:
            p1spaces.append(l)
    if p1tile[0] != columns[-1]:
        r = columns[columns.index(p1tile[0])+1]+p1tile[1]
        if r not in tiles and r not in p1spaces:
            p1spaces.append(r)
    if p1tile[0] != columns[0] and p1tile[1] != rows[-1]:
        bl = columns[columns.index(p1tile[0])-1]+rows[rows.index(p1tile[1])+1]
        if bl not in tiles and bl not in p1spaces:
            p1spaces.append(bl)
    if p1tile[1] != rows[-1]:
        bm = p1tile[0]+rows[rows.index(p1tile[1])+1]
        if bm not in tiles and bm not in p1spaces:
            p1spaces.append(bm) 
    if p1tile[0] != columns[-1] and p1tile[1] != rows[-1]:
        br = columns[columns.index(p1tile[0])+1]+rows[rows.index(p1tile[1])+1]
        if br not in tiles and br not in p1spaces:
            p1spaces.append(br)    

def play(board): # plays the game for 10 turns, letting player and AI place a tile each turn and displaying the appropriate message at the end
    for i in range(1,11):
        print("Turn:", i)
        print_board(board)
        P1tile = ""

        for i in P1spaces: # adds unique spaces to the list of spaces that player and AI can place tiles in
            if i in P2spaces and i not in shared:
                shared.append(i)

        if P1spaces != []: # player cannot place a tile when there are no spaces to place on
            while P1tile not in P1spaces:
                P1tile = input("Type a letter and number to place a tile in an empty space: ").upper() # accepts letters regardless of case
                if P1tile not in P1spaces:
                    print("You cannot place a tile there.")

            place_tile(P1tile, P1spaces, P1tiles, P2spaces)
            board[P1tile[0]][int(P1tile[1]) - 1] = "+" # updates board with player's tile

        if shared != []: # AI chooses a random shared space if there are any
            P2tile = rand.choice(shared)
        elif P2spaces != []:
            P2tile = rand.choice(P2spaces)
        if P2spaces != []:
            place_tile(P2tile, P2spaces, P2tiles, P1spaces)
            board[P2tile[0]][int(P2tile[1]) - 1] = "-" # updates board with AI's tile
    
    print_board(board)

    if len(P1tiles) > len(P2tiles): # lets player know if they won based on the difference between number of tiles placed by player and AI
        print("You Win!")
    elif len(P1tiles) < len(P2tiles):
        print("You Lose.")
    else:
        print("It's a Tie!")

print("Welcome to PyTurf!")
print("Cover as much ground as you can!")
play(game_board)