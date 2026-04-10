import pygame
from engine.Node import Node
from engine.Nodes.Sprite import SpriteNode
from engine.Nodes.PlayerNode import PlayerNode
from engine.Nodes.Camera import CameraNode

class Scene:
    def __init__(self, the_input):
        self.input = the_input
        self.root = Node(parent=None, children=[], name="Root", active=True)
    
    def Initialize(self):
        self.root.ready()

        ## If for example self.player is used, then you can access the node through scene.node. so kinda like a global node.

        self.player = PlayerNode(self.root, name="player 1",x=130, y=130)
        self.root.children.append(self.player)

        self.red_box = SpriteNode(self.player,texture="engine/TestAssets/ball.png",name="RedBox1", x=100, y=100, width=50, height=50)
        self.player.children.append(self.red_box)

        self.redball = SpriteNode(self.root, name="Red Ball", texture="engine/TestAssets/redBall.png", x=800, y=100, width=50, height=50, active=True)
        self.root.children.append(self.redball)
        
        self.camera = CameraNode(parent=self.root, x=0, y=0)
        self.camera.follow(self.player)
        self.root.children.append(self.camera)

        self.root.debug_print_tree()

    def update(self, delta, input):
        self._update_node(self.root, delta, self.input)
    
    def _update_node(self, node, delta, the_input):
        if node.active:
            node.update(delta, the_input)
            for child in node.children:
                child._update_node(child, delta, the_input)