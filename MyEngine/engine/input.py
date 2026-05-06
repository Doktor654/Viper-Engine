import pygame

class Input:
    def __init__(self):
        self.current_keys = None
        self.previous_keys = None

        self.current_mouse = None
        self.previous_mouse = None
    def update(self):
        ## Keys
        # Spara gamla state
        self.previous_keys = self.current_keys
        # Hämta nya
        self.current_keys = pygame.key.get_pressed()

        # Mouse
        self.previous_mouse = self.current_mouse
        self.current_mouse = pygame.mouse.get_pressed()

    def key_pressed(self, target_key):
        if self.current_keys[target_key]:
            return True       
        return False


    def key_pressed_once(self, target_key):
        if self.current_keys[target_key] and not self.previous_keys[target_key]:
            return True
        return False

    
    ## Mouse Functions
    def mouse_pressed(self, button=0):
        return self.current_mouse[button]


    def mouse_pressed_once(self, button=0):
        return (
            self.current_mouse[button] and
            not self.previous_mouse[button]
        )
    def get_mouse_position(self):
        return pygame.mouse.get_pos()