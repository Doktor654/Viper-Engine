import pygame
from engine.Node import Node
from engine.Nodes.Sprite import SpriteNode
from engine.Nodes.PlayerNode import PlayerNode

class Scene:
    def __init__(self, the_input):
        self.input = the_input
        self.root = Node(parent=None, children=[], name="Root", active=True)
    
    def Initialize(self):
        self.root.ready()

        player = PlayerNode(self.root, x=130, y=130)
        player.parent.children.append(player)

        red_box = SpriteNode(player,texture="engine/ball.png", x=100, y=100, width=50, height=50)
        red_box.parent.children.append(red_box)

    def update(self, delta, input):
        self._update_node(self.root, delta, self.input)
    
    def _update_node(self, node, delta, the_input):
        if node.active:
            node.update(delta, the_input)
            for child in node.children:
                child._update_node(child, delta, the_input)