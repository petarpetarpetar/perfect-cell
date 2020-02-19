#!/usr/bin/env python3
class Food():
    def  __init__(self, position):
        self.energy = 10
        self.position = position
        self.live = True
        self.destroy = False

    def update(self):
        return self.live
