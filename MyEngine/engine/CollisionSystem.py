import pygame

class CollisionSystem:
    def __init__(self, collision_bodies=[]):
        self.collision_bodies = collision_bodies
    
    def add_to_bodies(self, collision_bod):
        self.collision_bodies.append(collision_bod)

    def check_collisions(self):
        for A in self.collision_bodies:
            for B in self.collision_bodies:
                if A != B:
                    self.check_if_collide(A, B) 

    def check_if_collide(self, A, B):
        if A.get_rect() != None and B.get_rect() != None:
            if A.get_rect().colliderect(B.get_rect()):
                A.on_collision(B)
                B.on_collision(A)

    def clear_collisions(self):
        self.collision_bodies = []
        

