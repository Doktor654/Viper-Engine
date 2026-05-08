import pygame
from engine.Nodes.TransformNode import TransformNode


class CameraNode(TransformNode):
    def __init__(self,parent, children=[], name="Camera", active=True, x=0, y=0, centered=False):
        super().__init__(parent, children, name, active)
        self.position = [x, y]
        self.target = None
        self.smoothness = 0.1  # 0 = super slow, 1 = instant snap
        self.centered = centered

    def follow(self, target_node):
        self.target = target_node
        
    def set_position(self,x,y):
        self.position = [x,y]
    
    
    def _update_node(self, node, delta, the_input=None):
        #print("Camera:", self.position)
        if self.target is None:
            return

        # target position
        tx, ty = self.target.position

        # smooth follow (lerp)
        #lerp((self.position[0, self.position[1]]), ((tx - self.position[0]), (ty - self.position[1])), self.smoothness)
        self.position[0] += (tx - self.position[0]) * self.smoothness
        self.position[1] += (ty - self.position[1]) * self.smoothness