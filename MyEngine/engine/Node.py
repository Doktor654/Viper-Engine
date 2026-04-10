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
    def update(self, delta, the_input):
        for child in self.children:
            child.update(delta, the_input)
    def draw(self,screen):
        for child in self.children:
            child.draw(screen)

    ## DEBUGGING THE HIERARCHY TREE
    def debug_print_tree(self, depth=0):

        prefix = "  " * depth
        state = "\✓" if self.active else "/✗"

        print(f"{prefix}{state} {self.name}")

        for child in self.children:
            child.debug_print_tree(depth + 1)