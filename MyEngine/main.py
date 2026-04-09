import sys, pygame
## Import all the different parts
from engine.game_loop import GameLoop
from engine.Scene import Scene
from Renderer.renderer import Renderer
from engine.input import Input


## Initialize the scene, renderer and game_loop
## and then run the gameloop from there
the_scene = Scene()
the_input = Input()
the_renderer = Renderer(the_scene)
the_game_loop = GameLoop(the_scene, the_renderer, the_input)


the_game_loop.run(the_scene)

the_input.key_pressed(pygame.K_SPACE)




