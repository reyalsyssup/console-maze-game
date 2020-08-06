import copy, os, mazeGen

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
        elif self.state == "player": return "☺️"
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
                # populates each spot in the grid with a cell class
                col.append(copy.deepcopy(Cell("", "empty")))
            grid.append(col)
        self.grid = grid
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

    def toText(self):
        newArray = []
        for row in self.grid:
            newRow = []
            for i in row:
                newRow.append(i.render())
            newArray.append(newRow)
        return newArray
    
    def game(self):
        lastpos = player.pos()
        while True:
            clear()
            print(f"Your pos: {player.pos()}")
            mazeGen.genMaze(self.grid)
            self.render()
            move = input("Make a move (w, a, s, d): ")
            if move == "w": player.y += -1
            elif move == "s": player.y += 1
            elif move == "a": player.x += -1
            elif move == "d": player.x += 1
            # boundaries (modified to suite maze walls && border)
            print(self.grid[player.x][player.y].state)
            if self.grid[player.x][player.y].state == "wall":
                player.x = lastpos[0]; player.y = lastpos[1]
            # changes the player's previous positon back to empty
            self.grid[lastpos[1]][lastpos[0]].state = "empty"
            lastpos = player.pos()

if __name__ == "__main__":
    player = Player()
    board = Board(15, 15, player)
    board.game()