import pygame
from engine.Node import Node

class TransformNode(Node):
    def __init__(self, parent, children=[], name="PlayerNode", active=True):
        super().__init__(parent, children, name, active)

        self.position = [0,0]
        self.world_position = [0,0]

    def update(self, delta, input):
        self.update_transform()

        super().update(delta, input)

    def update_transform(self):
        if self.parent and hasattr(self.parent, "world_position"):
            self.world_position[0] = self.parent.world_position[0] + self.position[0]
            self.world_position[1] = self.parent.world_position[1] + self.position[1]
        else:
            self.world_position = self.position.copy()