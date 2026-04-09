import pygame

class Node:
    def __init__(self, parent, children, name, active):
        self.parent = parent
        self.children = children
        self.name = name
        self.active = active
    
    def ready(self):
        print(f"{self.name} initialized")
        for child in self.children:
            child.ready()
    def update(self, delta):
        for child in self.children:
            child.update(delta)
    def draw(self,screen):
        for child in self.children:
            child.draw(screen)
