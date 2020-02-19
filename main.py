#!/usr/bin/env python3

import pygame
import math
import time

import world
import cell
import food

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
        background = create_background(width, height)
        clock = pygame.time.Clock()
        the_world_is_a_happy_place = 0
        world.init(100,100)
        while True:
                the_world_is_a_happy_place += 1
                for event in pygame.event.get():
                        if is_trying_to_quit(event):
                                return

                draw_grid(screen, )
                pygame.display.flip()
                clock.tick(fps)


def draw_grid(surface, width, height):
        background_color = (0,0,0)
        pygame.draw.rect(surface,background_color , pygame.Rect(0,0, width, height))
        wofc = 2
        hofc = 2
        cellColor = (255,0,0)
        foodColor = (0,255,0)
        for c in world.cells:
                pygame.draw.rect(surface, cellColor, pygame.Rect(c.position[0]*wofc,c.position[1]*hofc , wofc, hofc))
        for f in world.foods:
                pygame.draw.rect(surface, foodColor, pygame.Rect(f.position[0]*wofc,f.position[1]*hofc , wofc, hofc))

main(300, 300, 60)
