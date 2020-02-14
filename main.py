#!/usr/bin/env python3

import pygame

import pygame
import math
import time

def create_background(width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        background = pygame.Surface((width, height))
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(
                                background,
                                colors[(row + col) % 2],
                                pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width
        return background

def is_trying_to_quit(event):
        pressed_keys = pygame.key.get_pressed()
        alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
        x_button = event.type == pygame.QUIT
        altF4 = alt_pressed and event.type == pygame.KEYDOWN and event.key == pygame.K_F4
        escape = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        return x_button or altF4 or escape

def main(width, height, fps):
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('press space to see next demo')
        background = create_background(width, height)
        clock = pygame.time.Clock()
        the_world_is_a_happy_place = 0
        grid = []
        for i in range(10):
            grid.append([])
            for j in range(10):
                grid[i].append((i+j)%10)
        print(grid)
        while True:
                the_world_is_a_happy_place += 1
                for event in pygame.event.get():
                        if is_trying_to_quit(event):
                                return
                draw_grid(screen, grid)
                pygame.display.flip()
                clock.tick(fps)


def draw_grid(surface, grid):
        width = 30
        height = 30
        color = (128, 0, 128) # purple
        for i in range( len( grid ) ):
            for j in  range( len( grid[0] ) ):
                if grid[i][j] == 1:
                    color = (255,255,255)
                elif grid[i][j] == 2:
                    color = (0,0,0)
                else:
                    color = (100,100,100)
                pygame.draw.rect(surface, color, pygame.Rect(i*width,j*height , width, height))

main(300, 300, 60)
