import pygame
from engine.Nodes.TransformNode import TransformNode
from engine.Nodes.Sprite import SpriteNode

class AnimatedSprite(TransformNode):
    def __init__(self, parent, children=[], name="AnimatedSprite", textures=[], duration=1, loop=True ,x=100, y=100, width=0, height=0, color=..., active=True, flip_y=False, flip_x=True):
        super().__init__(parent, children, name, active)
        self.position[0] = x
        self.position[1] = y
        self.width = width
        self.height = height
        self.textures = textures
        self.texture = None
        self.current_frame = 0
        self.frames = []
        self.duration = duration
        self.loop = loop
        self.currently_playing = False
        self.playing = True

        for texture in self.textures:
            self.frames.append(pygame.image.load(texture))
        
        self.texture = self.frames[self.current_frame]
        if self.width != 0 or self.height != 0:
            self.texture = pygame.transform.scale(self.texture, (self.width, self.height))
        
    def start(self):
        self.playing = True

    def loop_through_frames(self, delta):
        # If not started, start countdown.
        if not self.currently_playing and self.playing == True:
            self.count_down = self.duration
            self.currently_playing = True
        
        # If currently playing, loop through frames
        if self.playing == True:
            self.count_down -= delta
            # If count down is 0, change frame
            if self.current_frame == len(self.frames) - 1 and self.loop == False:
                self.currently_playing = False
                return
                
            elif self.loop == True or self.current_frame < len(self.frames) - 1:
                if self.count_down <= 0:
                    print("Change frame")
                    self.currently_playing = True
                    self.texture = pygame.transform.scale(self.frames[self.current_frame], (self.width, self.height))
                    self.current_frame = (self.current_frame + 1) % len(self.frames)
                    
                    self.count_down = self.duration
            
                
    def draw(self, screen, offset=(0, 0)):
        if self.texture != None:
            spriteRect = self.texture.get_rect()
            spriteRect.x = self.world_position[0] - offset[0]
            spriteRect.y = self.world_position[1] - offset[1]
            screen.blit(self.texture, spriteRect)
        else:
            pygame.draw.rect(screen, self.color, (self.world_position[0], self.world_position[1]))
    def update(self, delta, the_input):
        super().update(delta, the_input)
        
        self.loop_through_frames(delta)
        self.playing = True
    
    def _update_node(self, node, delta, the_input):
        if node.active:
            node.update(delta, the_input)
            for child in node.children:
                child._update_node(child, delta, the_input)