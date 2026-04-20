import pygame
from engine.Nodes.Sprite import SpriteNode
class ScrollingBackground(SpriteNode):
    def __init__(self, parent, texture, name="ScrollingBckg", x=0, y=0, width=800, height=600, speed=100, direction="horizontal", mode="scroll", camera=None):
        super().__init__(parent, texture=texture, name=name, x=x, y=y, width=width, height=height)
        self.speed = speed
        self.direction = direction
        self.mode = mode
        self.camera = camera

        if self.direction == "horizontal":
            self.bg2 = SpriteNode(parent, texture=texture, name="Background 2", x=x+width, y=y, width=width, height=height)
        else:
            self.bg2 = SpriteNode(parent, texture=texture, name="Background 2", x=x, y=y+height, width=width, height=height)
        
        parent.children.insert(0, self.bg2)

    def _update_node(self, node, delta, the_input):
        if self.mode == "scroll":
            self._scroll(delta)
        elif self.mode == "static" and self.camera:
            self._static()

    def _scroll(self, delta):
        if self.direction == "horizontal":
            self.position[0] -= self.speed * delta
            self.bg2.position[0] -= self.speed * delta
            if self.position[0] + self.width <= 0:
                self.position[0] = int(self.bg2.position[0] + self.width) - 3
            if self.bg2.position[0] + self.width <= 0:
                self.bg2.position[0] = int(self.position[0] + self.width) - 3
        else:
            self.position[1] -= self.speed * delta
            self.bg2.position[1] -= self.speed * delta
            if self.position[1] + self.height <= 0:
                self.position[1] = int(self.bg2.position[1] + self.height) - 3
            if self.bg2.position[1] + self.height <= 0:
                self.bg2.position[1] = int(self.position[1] + self.height) - 3

    def _static(self):
        if self.direction == "vertical":
            camera_top = self.camera.position[1] - (self.height / 2)
            camera_bottom = self.camera.position[1] + (self.height / 2)

            # Kameran åker neråt
            if self.position[1] + self.height < camera_top:
                self.position[1] = self.bg2.position[1] + self.height
            if self.bg2.position[1] + self.height < camera_top:
                self.bg2.position[1] = self.position[1] + self.height

            # Kameran åker uppåt
            if self.position[1] > camera_bottom:
                self.position[1] = self.bg2.position[1] - self.height
            if self.bg2.position[1] > camera_bottom:
                self.bg2.position[1] = self.position[1] - self.height