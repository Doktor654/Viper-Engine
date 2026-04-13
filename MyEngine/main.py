import sys, pygame
## Import all the different parts
from engine.game_loop import GameLoop
from engine.Scene import Scene
from Renderer.renderer import Renderer
from engine.input import Input
from engine.CollisionSystem import CollisionSystem


## Initialize the scene, renderer and game_loop
## and then run the gameloop from there
the_input = Input()
the_scene = Scene(the_input)
the_collision_system = CollisionSystem()


the_renderer = Renderer(the_scene, (400, 400))
the_game_loop = GameLoop(the_scene, the_collision_system ,the_renderer, the_input)


the_game_loop.run(the_scene)


