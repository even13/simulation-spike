
import itertools
import time

grid = [
["*", "-","-"],
["-", "*", "-"],
["-", "*","*"]
]

def print_grid():
    for row in grid:
        print("".join(row))

neighbours = lambda x, y : [
                            grid[(x-1)%3][(y+1)%3],
                            grid[x%3][(y+1)%3],
                            grid[(x+1)%3][(y+1)%3],
                            grid[(x-1)%3][y%3],
                            grid[(x+1)%3][y%3],
                            grid[(x-1)%3][(y-1)%3],
                            grid[x%3][(y-1)%3],
                            grid[(x+1)%3][(y-1)%3]
                            ]

def switch_dead_cell(num):
    switcher = {
        1: "-",
        2: "-",
        3: "-",
        4: "-",
        5: "*",
        6: "*",
        7: "-",
        8: "-"
    }
    return(switcher.get(num))

# tuple before grid
# neighbours = lambda x, y : [grid[(x-1)%3][(y+1)%3)], (x%3, (y+1)%3), ((x+1)%3, (y+1)%3), ((x-1)%3, y%3), ((x+1)%3, y%3), ((x-1)%3, (y-1)%3), (x%3, (y-1)%3), ((x+1)%3, (y-1)%3) ]

def rule_evol():
    for i, row in enumerate(grid, start = 0):
        for j, elt in enumerate(row, start = 0):
            # print("row is {} and i is {} and j is {} and element is {}".format(row, i, j, elt))
            # print("neighbours", neighbours(i, j))
            # print(neighbours(i,j).count("-"))
            # print("grid before", print_grid())
            grid[i][j] = switch_dead_cell(neighbours(i,j).count("-"))
            # print("grid after", print_grid())



while True:
    print_grid()
    print("")
    rule_evol()
    time.sleep(1)

# def check_neighbours(x, y):
#     neighbours = [
#     x,
#     y,
#     x+1,
#     x-1,
#     y+1,
#     y-1
#     ]
#     perm = itertools.combinations(neighbours, 2)
#     print(list(dict.fromkeys(perm)))
    # for i in list(perm):
    #     print(i)
# #
# print_grid()
# X = 10
# Y = 10



# neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
#                                for y2 in range(y-1, y+2)
#                                if (-1 < x <= X and
#                                    -1 < y <= Y and
#                                    (x != x2 or y != y2) and
#                                    (0 <= x2 <= X) and
#                                    (0 <= y2 <= Y))]

# print(neighbours(0, 0))

#
# check_neighbours(3,6)
