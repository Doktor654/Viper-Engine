import pygame
from engine.Nodes.TransformNode import TransformNode

class PlayerNode(TransformNode):
    def __init__(self, parent, children=[], name="PlayerNode", x=0, y=0, active=True):
        super().__init__(parent, children or [], name, active)
        self.position[0] = x
        self.position[1] = y


    def _update_node(self, node, delta, the_input):
        if node.active:
            node.update(delta, the_input)
            for child in node.children:
                child._update_node(child, delta, the_input)

            if the_input.key_pressed(pygame.K_UP):
                self.position[1] -= 100 * delta
               # print("Up ", self.position[1])
            if the_input.key_pressed(pygame.K_DOWN):
                
                self.position[1] += 100 * delta
                #print("Down ", self.position[1])
            if the_input.key_pressed(pygame.K_LEFT):
                
                self.position[0] -= 100 * delta
                #print("LEFT ", self.position[0])
            if the_input.key_pressed(pygame.K_RIGHT):
                
                self.position[0] += 100 * delta
                #print("RIGHT ", self.position[0])

            if the_input.key_pressed_once(pygame.K_SPACE):
                self.position[1] -= 1000 * delta
                print("once jump")