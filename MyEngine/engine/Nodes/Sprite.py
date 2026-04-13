import pygame
from engine.Nodes.TransformNode import TransformNode

class SpriteNode(TransformNode):
    def __init__(self, parent, children=[], name="Sprite", texture=None, x=100, y=100, width=0, height=0, color=(255,255,255), active=True, flip_y=False):
        super().__init__(parent, children or [], name, active)
        self.position[0] = x
        self.position[1] = y
        self.width = width
        self.height = height
        self.color = color
        self.texture = texture

        if texture != None:
            self.texture = pygame.image.load(texture)
            if self.width != 0 or self.height != 0:
                self.texture = pygame.transform.scale(self.texture, (self.width, self.height))
        else:
            self.texture = None
        
        if flip_y:
            self.texture = pygame.transform.flip(self.texture, False, True)

    def draw(self, screen, offset=(0, 0)):
        if self.texture != None:
            spriteRect = self.texture.get_rect()
            spriteRect.x = self.world_position[0] - offset[0]
            spriteRect.y = self.world_position[1] - offset[1]
            screen.blit(self.texture, spriteRect)
        else:
            pygame.draw.rect(screen, self.color, (self.world_position[0], self.world_position[1]))
    
    def _update_node(self, node, delta, the_input):
        if node.active:
            node.update(delta, the_input)
            for child in node.children:
                child._update_node(child, delta, the_input)