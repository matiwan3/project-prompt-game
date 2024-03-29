#!/usr/bin/env python3
import random

class UnitArcher:
    def __init__(self):
        self.health = 1
        self.strength = 3 
        self.stamina = 4
        self.intelligence = 1
        self.luck = 1
        self.tool = 'Bow'
        self.inventory = {}
        self.gold = random.randint(0,100)
    
    def getStats(self):
        return {
            'health': self.health,
            'armor': self.armor,
            'strength': self.strength,
            'stamina': self.stamina,
            'tool': self.tool,
            'gold': self.gold
        }
