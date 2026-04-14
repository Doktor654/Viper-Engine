import pygame

class Renderer:
    def __init__(self, scene, size=[400,400]):
        self.scene = scene
        self.size = (size[0], size[1])
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("PyGame Engine")

    def draw(self, scene):
        self.screen.fill((128, 128, 128))

        self._draw_node(self.scene.root)
        
        self._draw_UI(self.scene.root)

        pygame.display.flip()

    def _draw_node(self, node):
        if not node.active:
            return

        if hasattr(node,"screen_space"):
            return
        offset = (0, 0)

        if self.scene.camera:
            offset = (
                self.scene.camera.position[0] - (self.size[0] /2),
                self.scene.camera.position[1] - (self.size[1] / 2)
            )

        node.draw(self.screen, offset)

        for child in node.children:
            self._draw_node(child)
    
    def _draw_UI(self, node):
        if not node.active:
            return

        if hasattr(node,"screen_space"):
            if node.screen_space==True:
                node.draw(self.screen)

        for child in node.children:
            self._draw_UI(child)