import pygame

class Renderer:
    def __init__(self, scene):
        self.scene = scene
    def draw(self, scene):
        size = width, height = 320, 240
        speed = [2, 2]
        black = 0, 0, 0
        grey = 128, 128, 128

        screen = pygame.display.set_mode(size)
        
        screen.fill(grey)
        pygame.display.flip()