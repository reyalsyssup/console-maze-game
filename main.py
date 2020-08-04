import copy, os

def clear():
    # windows
    if os.name == "nt": os.system("cls")
    # linux/mac
    else: os.system("clear")

class Player:
    def __init__(self):
        self.x = 1
        self.y = 1
    def pos(self):
        return (self.x, self.y)

class Cell:
    def __init__(self, look, state="wall"):
        self.look = look
        self.state = state
    def render(self):
        if self.state == "wall": return "#"
        # chr(9617) returns this: ░
        elif self.state == "empty": return chr(9617)
        elif self.state == "player": return "*"
        else: return "something went wrong"

class Board:
    def __init__(self, width, height, player, spacing=1):
        self.width = width
        self.height = height
        self.player = player
        self.spacing = spacing
        grid = []
        for i in range(height):
            col = []
            for i in range(width):
                col.append(copy.deepcopy(Cell("", "empty")))
            grid.append(col)
        self.grid = grid
    
    def init(self):
        for row in range(len(self.grid)):
            for i in range(len(self.grid[row])):
                # sets the walls
                if row == 0 or i == 0 or i == self.width-1 or row == self.height-1:
                    self.grid[row][i].state = "wall"
                else: self.grid[row][i].state = "empty"

    def render(self):
        spacing = ""
        for i in range(self.spacing): spacing+=" "
        for row in range(len(self.grid)):
            for i in range(len(self.grid[row])):
                if player.pos()[0] == i and player.pos()[1] == row:
                    self.grid[row][i].state = "player"
                print(self.grid[row][i].render(), end=spacing)
            print()
    
    def game(self):
        self.init()
        lastpos = player.pos()
        while True:
            clear()
            print(f"You pos: {player.pos()}")
            self.render()
            move = input("Make a move (w, a, s, d): ")
            if move == "w": player.y += -1
            elif move == "s": player.y += 1
            elif move == "a": player.x += -1
            elif move == "d": player.x += 1
            # boundaries
            if player.pos()[0] < 1 or player.pos()[0] > self.width-2 or player.pos()[1] < 1 or player.pos()[1] > self.height-2:
                player.x = lastpos[0]; player.y = lastpos[1]

            self.grid[lastpos[1]][lastpos[0]].state = "empty"
            lastpos = player.pos()

player = Player()
board = Board(7, 7, player)
board.game()