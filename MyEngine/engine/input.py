import pygame

class Input:
    def __init__(self):
        self.current_keys = None
        self.previous_keys = None

    def update(self):
        # Spara gamla state
        self.previous_keys = self.current_keys

        # Hämta nya
        self.current_keys = pygame.key.get_pressed()

    def key_pressed(self, target_key):
        if self.current_keys[target_key]:
            return True       
        return False

   #def key_pressed_once(self, target_key):
   #    if self.current_keys[target_key]:
   #        self.current_keys = None
   #        return True
   #    return False