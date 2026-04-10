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

        player = PlayerNode(self.root, name="player 1",x=130, y=130)
        player.parent.children.append(player)

        red_box = SpriteNode(player,texture="engine/ball.png",name="RedBox1", x=100, y=100, width=50, height=50)
        red_box.parent.children.append(red_box)

        player2 = PlayerNode(self.root, name="player 2", x=50, y=130, active=False)
        player2.parent.children.append(player2)

        red_box2 = SpriteNode(player2,texture="engine/ball.png",name="RedBox2", x=100, y=100, width=50, height=50, active=False)
        red_box2.parent.children.append(red_box2)

        self.root.debug_print_tree()

    def update(self, delta, input):
        self._update_node(self.root, delta, self.input)
    
    def _update_node(self, node, delta, the_input):
        if node.active:
            node.update(delta, the_input)
            for child in node.children:
                child._update_node(child, delta, the_input)