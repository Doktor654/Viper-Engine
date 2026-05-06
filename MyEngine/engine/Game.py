import pygame
from engine import *

class Game():
    def __init__(self, scenes={"Scene" : Scene}, start_scene=None ,screen_size=(800, 600), fullscreen=False, fps=60):
        self.screen_size = screen_size
        self.fullscreen = fullscreen
        self.start_scene=start_scene
        self.fps = fps

        self.the_input = Input()
        self.scene_manager = SceneManager(available_scenes=scenes, current_scene=start_scene)
        self.scene = scenes[start_scene](self.the_input, self.scene_manager)
        self.the_collision_system = CollisionSystem()
        self.the_renderer = Renderer(self.scene, self.screen_size, fullscreen=self.fullscreen)
        self.the_game_loop = GameLoop(self.scene, self.the_collision_system ,self.the_renderer, self.the_input, fps=self.fps)
        self.scene_manager.get_needed_stuff(self.the_input, self.the_renderer, self.the_game_loop, self.the_collision_system)
    def run(self):
        self.the_game_loop.run(self.scene)