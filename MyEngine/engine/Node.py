import pygame

class Node:
    def __init__(self, parent, children, name, active):
        self.parent = parent
        self.children = children
        self.name = name
        self.active = active
    
    def ready(self):
        print("initialized")
    def update(self, delta):
        pass
    def draw(self):
        pass
