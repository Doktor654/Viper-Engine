import pygame
from engine.Node import Node
from engine.Nodes.Sprite import SpriteNode

class Scene:
    def __init__(self, the_input):
        self.input = the_input
        self.root = Node(parent=None, children=[], name="Root", active=True)
    
    def Initialize(self):
        self.root.ready()

        red_box = SpriteNode(self.root,texture="engine/ball.png", x=100, y=100)
        self.root.children.append(red_box)

    def update(self, delta, input):
        self._update_node(self.root, delta, self.input)
    
    def _update_node(self, node, delta, the_input):
        if node.active:
            node.update(delta, the_input)
            for child in node.children:
                child._update_node(child, delta, the_input)