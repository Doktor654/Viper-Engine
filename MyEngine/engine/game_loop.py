import pygame

class GameLoop:
    def __init__(self, scene, renderer):
        self.scene = scene
        self.renderer = renderer
        self.clock = pygame.time.Clock()
        self.Running = False

    ## Function that runs the looping, updates the scene and the render
    def run(self, scene, fps=60):
        self.Running = True
        while self.Running:
            delta = self.clock.tick(fps) / 1000.0
            
            #self.scene.update(delta) ## update the scene
            self.renderer.draw(self.scene)
            print(fps,"  ",delta)

    def end(self, scene):
        self.Running = False