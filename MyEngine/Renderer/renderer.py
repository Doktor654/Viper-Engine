import pygame
import os


class Renderer:
    def __init__(self, scene, size=(400, 400), fullscreen=False):
        self.scene = scene
        self.base_size = size  # virtual resolution

        self.fullscreen = fullscreen

        # SCREEN SETUP
        if self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.base_size, pygame.RESIZABLE)

        self.screen_size = self.screen.get_size()

        # ALWAYS create game_surface (THIS was your bug)
        self.game_surface = pygame.Surface(self.base_size)

        icon_path = os.path.join(os.path.dirname(__file__), "ViperLogo2.ico")
        if os.path.exists(icon_path):
            pygame.display.set_icon(pygame.image.load(icon_path))
        else:
            print("NO icon found")

        pygame.display.set_caption("Viper")

    def draw(self, scene):
        # update window size
        self.screen_size = self.screen.get_size()

        # clear virtual world
        self.game_surface.fill((128, 128, 128))

        # draw world
        self._draw_node(self.scene.root)
        self._draw_ui(self.scene.root)

        # SCALE LOGIC
        if self.fullscreen:
            # fullscreen = stretch to screen
            final = pygame.transform.scale(self.game_surface, self.screen_size)
            pos = (0, 0)
        else:
            # windowed = scale to window size
            final = pygame.transform.scale(self.game_surface, self.screen_size)
            pos = (0, 0)

        # render
        self.screen.blit(final, pos)
        pygame.display.flip()

    def _draw_node(self, node):
        if not node.active:
            return

        if getattr(node, "screen_space", False):
            return

        # camera ALWAYS based on virtual resolution
        offset = (0, 0)

        if self.scene.camera:
            if self.scene.camera.centered:
                offset = (
                    self.scene.camera.position[0] - (self.base_size[0] / 2),
                    self.scene.camera.position[1] - (self.base_size[1] / 2)
                )
            else:
                offset = (
                    self.scene.camera.position[0],
                    self.scene.camera.position[1]
                )

        node.draw(self.game_surface, offset)

        for child in node.children:
            self._draw_node(child)

    def _draw_ui(self, node):
        if not node.active:
            return

        if getattr(node, "screen_space", False):
            node.draw(self.game_surface)

        for child in node.children:
            self._draw_ui(child)