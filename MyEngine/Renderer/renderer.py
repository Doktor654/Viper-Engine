import pygame

class Renderer:
    def __init__(self, scene):
        self.scene = scene
        self.size = (800, 800)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("PyGame Engine")
    def draw(self, scene):
        speed = [2, 2]
        black = 0, 0, 0
        grey = 128, 128, 128

        self.screen.fill(grey)
        self._draw_node(self.scene.root, self.screen)
        pygame.display.flip()

    def draw_node(self, node, screen):
        _draw_node(node, self.screen)

    def _draw_node(self, node, screen):
        if node.active:
            node.draw(self.screen)
            for child in node.children:
                self._draw_node(child, self.screen)