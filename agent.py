#!/usr/bin/env python3

import grid

class Agent():
    @classmethod
    def __init__(self,dnk,position,):
        self.position = position
        self.dnk = dnk
        encode(dnk)
        # self.speed
        self.reproduction = 0
        self.age = 0
        # self.hunger
        self.energy = 100

    def encode(dnk):
        self.max_energy = 100
        self.max_speed = 1
        self.sight = 3
        self.color = (255,0,0)
        self.max_age = 100
        self.max_reproduction = 3

    def move((dx,dy)):
        pass
    def eat(food):
        pass
