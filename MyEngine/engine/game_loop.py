import pygame

class GameLoop:
    def __init__(self, scene, renderer, input):
        self.scene = scene
        self.renderer = renderer
        self.input = input
        self.clock = pygame.time.Clock()
        self.Running = False
        

    ## Function that runs the looping, updates the scene and the render
    def run(self, scene, fps=60):
        self.Running = True
        self.scene.Initialize()
        
        
        while self.Running:
            delta = self.clock.tick(fps) / 1000.0
            
            self.input.update()
            self.scene.update(delta, self.input)
            self.renderer.draw(self.scene)
            
            ## Test to switch camera
            if self.input.key_pressed_once(pygame.K_SPACE):
                self.scene.camera.follow(scene.player2)

            # Closing the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end()
            
            # On input
            #self.input.key_pressed(pygame.K_SPACE)
            #print("Fps and Delta : ", fps,"  ",delta)

    def end(self):
        self.Running = False