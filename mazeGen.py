test = [
    ["#","#","#","#","#"],
    ["#",".",".",".","#"],
    ["#",".",".",".","#"],
    ["#",".",".",".","#"],
    ["#","#","#","#","#"],
]

def render(array):
    for row in array:
        for i in row:
            print(i, end=" ")
        print()

render(test)