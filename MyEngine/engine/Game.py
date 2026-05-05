import pygame
from engine import *

class Game():
    def __init__(self, scene, screen_size=(800, 600), fullscreen=False, fps=60):
        self.screen_size = screen_size
        self.fullscreen = fullscreen
        self.fps = fps

        self.the_input = Input()
        self.scene = scene(self.the_input)
        self.the_collision_system = CollisionSystem()
        self.the_renderer = Renderer(self.scene, self.screen_size, fullscreen=self.fullscreen)
        self.the_game_loop = GameLoop(self.scene, self.the_collision_system ,self.the_renderer, self.the_input, fps=self.fps)
    
    def run(self):
        self.the_game_loop.run(self.scene)