import pygame
from engine.Node import Node

class SpriteNode(Node):
    def __init__(self, parent, children=[], name="Sprite", x=100, y=100, width=30, height=30, color=(255,255,255), active=True):
        self.parent = parent
        self.children = children
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.active = active
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def _update_node(self, node, delta):
        if node.active:
            node.update(delta)
            for child in node.children:
                child._update_node(child, delta)