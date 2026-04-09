import pygame
from engine.Node import Node

class SpriteNode(Node):
    def __init__(self, parent, children=[], name="Sprite", texture=None, x=100, y=100, width=30, height=30, color=(255,255,255), active=True):
        super().__init__(parent, children or [], name, active)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.texture = texture
    def draw(self, screen):
        if self.texture != None:
            spriteTexture = pygame.image.load(self.texture)
            spriteRect = spriteTexture.get_rect()
            spriteRect.x = self.x
            spriteRect.y = self.y
            screen.blit(spriteTexture, spriteRect)
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def _update_node(self, node, delta):
        if node.active:
            node.update(delta)
            for child in node.children:
                child._update_node(child, delta)