import pygame
from engine.Nodes.TransformNode import TransformNode
from engine.CollisionSystem import CollisionSystem

class CollisionBody(TransformNode):
    def __init__(self, parent, children=[], name="CollisionBody",color=(100,100,100) ,x=0, y=0, active=True, width=0, height=0, collision_type="Rect", static=True):
        super().__init__(parent, children or [], name, active)
        self.world_position[0] = x
        self.world_position[1] = y

        self.color = color

        self.width = width
        self.height = height
        self.collision_type = collision_type
        self.static=static
        self.body = None

    def draw(self, screen, offset=(0, 0)):
        if self.collision_type == "Rect":
            x = self.world_position[0] - offset[0]
            y = self.world_position[1] - offset[1]
            # skapa transparent surface
            surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

            # rita med alpha
            pygame.draw.rect(surface, (self.color), (0, 0, self.width, self.height))

            # rita ut på screen
            self.body = screen.blit(surface, (x, y))
    def _update_node(self, node, delta, the_input):
        pass
    def on_collision(self, other):
        if other.static:
            self.parent.collided(self.get_rect(), other.get_rect())
            
        print("%s Collided with %s" % (self.name, other.name))

    def get_rect(self):
        if self.body != None:
            return self.body