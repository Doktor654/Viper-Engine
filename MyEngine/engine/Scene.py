import pygame
from engine.Node import Node
from engine.Nodes.Sprite import SpriteNode

class Scene:
    def __init__(self):
        self.root = Node(parent=None, children=[], name="Root", active=True)
    
    def Initialize(self):
        self.root.ready()

        red_box = SpriteNode(self.root, x=100, y=100)
        self.root.children.append(red_box)

    def update(self, delta):
        self._update_node(self.root, delta)
    
    def _update_node(self, node, delta):
        if node.active:
            node.update(delta)
            for child in node.children:
                child._update_node(child, delta)