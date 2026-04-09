import pygame
from engine.Node import Node

class Scene:
    def __init__(self,):
        self.root = Node(parent=None, children=[], name="Root", active=True)
    
    def Initialize(self):
        self.root.ready()

    def update(self):
        self._update_node(self, node)
    
    def _update_node(self, node ):
        if node.active:
            node.update()
            for child in node.children:
                child._update_node(child, )

    def draw_node(self, node):
        self._draw_node(node)

    def _draw_node(self, node):
        if node.active:
            node.draw()
            for child in node.children:
                draw_node(child)