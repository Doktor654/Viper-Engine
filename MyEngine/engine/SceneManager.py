import pygame

from engine import *

class SceneManager():
    def __init__(self, available_scenes={"Scene" : Scene}, current_scene=None):
        self.current_scene = current_scene
        self.available_scenes = available_scenes

        self.previous_scene : Scene = None

    def get_needed_stuff(self, the_input, the_renderer, the_game_loop, the_collision_system):
        self.the_input = the_input
        self.the_renderer = the_renderer
        self.the_game_loop = the_game_loop
        self.the_collision_system = the_collision_system

    ## Function for switching scenes
    def go_to(self, target_scene):
        if target_scene not in self.available_scenes.keys():
            print("Scene not found : ", target_scene, "  Scenes : ", self.available_scenes.keys())
            return

        print("Switch scene to target_Scene : ", target_scene, "  Scenes : ", self.available_scenes.keys())
        target = self.available_scenes[target_scene](self.the_input, self)
        self.previous_scene = self.current_scene
        self.current_scene = target
        self.the_renderer.scene = self.current_scene
        self.current_scene.Initialize(self.the_collision_system)
        self.the_collision_system.clear_collisions()
        self.the_game_loop.scene = self.current_scene

     ## Help functions
    def get_current_scene(self):
        return self.current_scene
    def get_previous_scenes(self):
        return self.previous_scene
    def get_available_scenes(self):
        return self.available_scenes