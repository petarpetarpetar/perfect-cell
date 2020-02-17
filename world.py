#!/usr/bin/env python3


w = 0
h = 0

grid = []
def init(i,j):
    w = i
    h = j
    for i in range(w):
        grid.append([])
        for j in range(h):
            grid[i].append('#')
def get(i,j):
    if i > 0 and i < w and j > 0 and j < h:
        return grid[i][j]
    else:
        return False
print(grid)
