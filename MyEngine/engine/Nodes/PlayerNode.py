import pygame
from engine.Nodes.TransformNode import TransformNode

class PlayerNode(TransformNode):
    def __init__(self, parent, children=[], name="PlayerNode", x=0, y=0, active=True):
        
        super().__init__(parent, children or [], name, active)
            
        self.position[0] = x
        self.position[1] = y

        self.colliding = False
        self.colliding_x = False
        self.colliding_y = False


    def collided(self, my_rect, other_rect):
        overlap_x_left  = other_rect.right - my_rect.left 
        overlap_x_right = my_rect.right - other_rect.left 
        overlap_y_top   = other_rect.bottom - my_rect.top
        overlap_y_bot   = my_rect.bottom - other_rect.top

        min_x = overlap_x_left if overlap_x_left < overlap_x_right else -overlap_x_right
        min_y = overlap_y_top  if overlap_y_top  < overlap_y_bot   else -overlap_y_bot

        if abs(min_x) < abs(min_y):
            self.colliding_x = True
            self.position[0] += min_x*0.1  # skjut ut direkt
            self.update_transform()
        else:
            self.colliding_y = True
            self.position[1] += min_y *0.1 # skjut ut direkt
            self.update_transform()

    
    def _update_node(self, node, delta, the_input):
        if node.active:
            # Spara INNAN rörelse
            self.old_position_x = self.position[0]
            self.old_position_y = self.position[1]

            for child in node.children:
                child._update_node(child, delta, the_input)

        #    if not self.colliding_y:
        #        if the_input.key_pressed(pygame.K_UP):
        #            self.position[1] -= 100 * delta
        #        if the_input.key_pressed(pygame.K_DOWN):
        #            self.position[1] += 100 * delta
        #    if not self.colliding_x:
        #        if the_input.key_pressed(pygame.K_LEFT):
        #            self.position[0] -= 100 * delta
        #        if the_input.key_pressed(pygame.K_RIGHT):
        #            self.position[0] += 100 * delta

            self.colliding_x = False
            self.colliding_y = False