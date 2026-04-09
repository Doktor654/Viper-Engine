import pygame

class Input:
    def __init__(self):
        pass

    def update(self):
        pass
    
    def key_pressed(self, target_key):
        keys = pygame.key.get_pressed()

        if keys[target_key]:
            print("Target_key_hit")
            return True
        
        return False