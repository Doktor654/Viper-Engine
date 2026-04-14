import pygame
from engine.Nodes.TransformNode import TransformNode

class UINode(TransformNode):
    def __init__(self, parent, children=[], name="UI", x=100,y=100, width=0, height=0, active=True, screen_space=True):
        super().__init__(parent, children or [], name, active)

        self.position[0]=x
        self.position[1]=y
        self.width = width
        self.height = height
        self.active = active
        self.screen_space= screen_space
