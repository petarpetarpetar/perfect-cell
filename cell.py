#!/usr/bin/env python3

import enum
import random
import math
#enable debug mode in order to get useful prints prints
_debugMode = False

worldWidth = 1000
worldHeight = 700

class state(enum.Enum):
    NULL = -1
    SEARCING4FOOD = 0
    SEARCING4PARNTER = 1
    GOING4FOOD = 2
    GOING4PARTNER = 3
    EATING = 4
    FIGHTING = 5

class Cell():
    def decode(self,decodeWhat):
        def dec_viewRange():
            dnkExtract = self.dnk[:4]
            for ch in dnkExtract:
                self.viewRange += ord(ch) - 97
            
            if _debugMode:
                print("assigned starting value to cell's viewRange = ", self.viewRange)
            pass
        
        def dec_speed():
            dnkExtract = self.dnk[4:8]

            for ch in dnkExtract:
                self.speed += ord(ch) - 97
            if _debugMode:
                print("assigned starting value to cell's speed = ", self.speed)
            pass

        def dec_matingScore():
            dnkExtract = self.dnk[8:12]

            for ch in dnkExtract:
                self.matingScore += ord(ch) - 97
            if _debugMode:
                print("assigned starting value to cell's matingScore = ", self.matingScore)
            pass

        def dec_wantingScore():
            dnkExtract = self.dnk[12:16]

            for ch in dnkExtract:
                self.wantingScore += ord(ch) - 97
            if _debugMode:
                print("assigned staring value to cell's wantingScore = ", self.wantingScore)
            pass

        def dec_maxAge():
            dnkExtract = self.dnk[16:20]

            for ch in dnkExtract:
                self.maxAge += ord(ch) - 97
            if _debugMode:
                print("assigned starting value to cell's maxAge = ", self.maxAge)
            pass    

        def dec_maxReproduction():
            dnkExtract = self.dnk[20:24]

            for ch in dnkExtract:
                self.maxReproduction += ord(ch) - 97
            if _debugMode:
                print("assigned starting value to cell's maxReproduction = ", self.maxReproduction)
            pass

        switcher = {
            0:dec_viewRange,
            1:dec_speed,
            2:dec_matingScore,
            3:dec_wantingScore,
            4:dec_maxAge,
            5:dec_maxReproduction
        }        
        func = switcher.get(decodeWhat, lambda : 'invalid decodeWhat')
        return func()
    # @brief constructor for when a new cell is generated at the beggining of simulation (random gen era)
    def __init__(self,position, dnk, id):
        self.id = id                        #id of a cell in order to keep track of numbers and identifying the cells
        self.position = position            #current position of the cell
        self.dnk = dnk                      #dnk sequence of a cell
        self.age = 0                        #age of a cell (how much cycles it has lived)
        self.energy = 80                    #energy of a cell (used for actions like: surviving next cycle, eating, searcing, moving...)
        self.reporductionCount = 0          #how much generations has this cell already produced
        self.target = None                  #cell is currently moving to target (food, or partner)
        self.cellState = state.NULL         #state of a cell (declared in an enum above the cell class)
        self.viewRange = self.decode(0)          #a range of detection of other cells and food units 
        self.speed = self.decode(1)              #speed(in tiles) which cell can move (greater speed requires greater energy spent)
        self.matingScore = self.decode(2)        #starting mating score (yet to be declared if it's going to be in dnk or calculated using speed and age)
        self.wantingScore = self.decode(3)       #wanting score for pair mating (hopefully represents races of cells)
        self.maxAge = self.decode(4)             #age of cell and it's going to die if it doesn't have enough energy to expand it's max age
        self.maxReproduction = self.decode(5)    #to stop over populating everything

    # @brief method for decoding values from dnk sequence to values inside cell
    

    # @brief determinating how the cell moves
    def move(self,movePos):
        if  not(0 < self.position[0] + movePos[0] < worldWidth):
            if _debugMode:
                print("cell.move(movePos) => cell has hit a horizontal wall")
            return False
        
        if not(0 < self.position[1]  + movePos[1] < worldHeight):
            if _debugMode:
                print("cell.mvoe(movePos) => cell has hit a vertical wall")
            return False
        pass

        self.position[0] += movePos[0]
        self.position[1] += movePos[1]

        self.energy -= movePos[0]**2 + movePos[1]**2
        if _debugMode:
            print("move(movePos): energy reduced by:",movePos[0]**2 + movePos[1]**2)
        return True

    def eat(self,food):
        self.energy += food.energy
        pass


    def update(self):

        def calculateDistance(a,b,self):
            return math.sqrt(abs(a[0]-b[0])**2 + abs(a[1] - b[1])**2)
            
        if self.cellState == state.SEARCING4FOOD:
            seedDirection = random.randint(1,4)
            seedDistance = random.randint(0,self.speed)
            if seedDirection == 1:
                self.move((self.speed, 0))
            
            elif seedDirection == 2:
                self.move((0, self.speed))
            
            elif seedDirection == 3:
                self.move(((-1)*self.speed,0))
            
            elif seedDirection == 4: 
                self.move((0,(-1)*self.speed))
            
            ###SCAN
            world_cellList = []
            world_foodList = []
            if self.cellState == state.SEARCING4FOOD:
                for world_food in world_foodList:
                    if _debugMode:
                        print("update()>search => examining food")
                    if calculateDistance(self.position, world_food.position,self) <= self.viewRange:
                        self.cellState = state.GOING4FOOD
                        self.target = world_food.position

            elif self.cellState == state.SEARCING4PARNTER:
                for world_cell in world_cellList:
                    if _debugMode:
                        print("update()>search => examining cell#", world_cell.id)
                    if calculateDistance(self.position, world_cell.position,self) <= self.viewRange:
                        print("WARNING: FOUND PARTNER> IT'S BAD IMPLEMENTATION SINCE CELLS MOVE, SHOULD FIX THIS BEFORE CONTINUING WITH MATING CODE, see coments")
                        #self.target should target id instead of position and keep track of the cell and if it goes out of sight. check mating score.
                        self.cellState = state.GOING4PARTNER
                        self.target = world_cell.position

        
        elif self.cellState == state.GOING4FOOD  or self.cellState == state.GOING4PARTNER:
            dist = calculateDistance(self.position, self.target,self)
            if  dist <= self.speed:
                self.move(self.target)
            else:
                difX = abs(self.position[0]-self.target[0])
                difY = abs(self.position[1]-self.target[1])
                moveX = (difX * self.speed) / dist
                moveY = (difY * self.speed) / dist
                self.move((moveX,moveY))
                if calculateDistance(self.position, self.target,self) <= 2:
                    self.cellState = state.EATING
            pass
            
print("radi")   