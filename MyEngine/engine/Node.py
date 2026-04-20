import pygame

class Node:
    def __init__(self, parent, children, name, active):
        self.parent = parent
        self.children = children
        self.name = name
        self.active = active
    
    def ready(self):
        print(f"{self.name} initialized")
        for child in self.children:
            child.ready()
    def update(self, delta, the_input):
        for child in self.children:
            child.update(delta, the_input)
    
    ## Passing value to avoid errors
    def draw(self, screen, offset=(0, 0)):
        pass

    def _update_node(self, node, delta, the_input):
        '''node, delta, input'''
        if node.active:
            node.update(delta, the_input)
            for child in node.children:
                child._update_node(child, delta, the_input)

    def collided(self, my_rect, other_rect):
        pass

    def remove_from_scene(self, collision_system=None):
        if self.parent and self in self.parent.children:
            self.parent.children.remove(self)
        
        if collision_system:
            self._remove_collisions(collision_system)

    def _remove_collisions(self, collision_system):
        from engine.Nodes.CollisionBody import CollisionBody
        if isinstance(self, CollisionBody) and self in collision_system.collision_bodies:
            collision_system.collision_bodies.remove(self)
        for child in self.children:
            child._remove_collisions(collision_system)

    ## DEBUGGING THE HIERARCHY TREE
    def debug_print_tree(self, depth=0):

        prefix = "  " * depth
        state = "\✓" if self.active else "/✗"

        print(f"{prefix}{state} {self.name}")

        for child in self.children:
            child.debug_print_tree(depth + 1)