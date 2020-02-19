#!/usr/bin/env python3
import cell
import food
import string
import random

width = 0
height = 0
cells = []
foods = []
cellCount = 0
def randomDNK(size):
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for i in range(size))

## initialization
#
#
def init(w, h, nc, nf):
    global cellCount
    weight = w
    height = h
    for _ in range(nc):
        position = [random.randrange(w),random.randrange(h)]
        cells.append(cell.Cell(position,randomDNK(24),cellCount))
        cellCount += 1
    for _ in range(nf):
        position = [random.randrange(w),random.randrange(h)]
        foods.append(food.Food(position))

## update cycle
#
def update():
    for i, c in enumerate(cells):
        live = c.update()
        if not live:
           cells.pop(i)
    for i, f in enumerate(foods):
        if not f.update():
            foods.pop(i)
    for i in random.randrange(2):
        position = [random.randrange(width),random.randrange(height)]
        foods.append(food.Food(position))
    pass
