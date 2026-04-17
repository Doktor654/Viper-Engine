import pygame
from engine.Nodes.UINode import UINode

class LabelNode(UINode):
    def __init__(self, parent, children=[], name="Label", text="Put Text Here",font="monospace",font_size=16,x=100,y=100, width=0, height=0, active=True, screen_space=True):
        super().__init__(parent, children or [], name, x, y, width, height, active, screen_space)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active = active
        self.text = text

        # Fonts
        self.font = font
        self.font_size = font_size
        self.my_font = pygame.font.SysFont(self.font, self.font_size)


    def draw(self, screen):
        

        my_label = self.my_font.render(self.text, 1, (155,0,0) )
        screen.blit(my_label, (self.x,self.y))        

    def _update_node(self, node, delta, the_input):
        if node.active:
            node.update(delta, the_input)
            for child in node.children:
                child._update_node(child, delta, the_input)
