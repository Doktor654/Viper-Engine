import pygame
from engine.Nodes.UINode import UINode

class ButtonNode(UINode):
    def __init__(self, parent, children=[], name="Button",color=(155,155,155), text_color=(155,155,155),text_align="Center" ,text="Button Text",font="monospace",font_size=16,x=100,y=100, width=0, height=0, active=True, screen_space=True):
        super().__init__(parent, children or [], name, active, x, y, screen_space)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active = active
        self.color=color


        self.text = text
        self.text_align = text_align
        self.text_color = text_color
        self.font = font
        self.font_size = font_size
        self.button_rect = None# BUtton rect
        self.my_font = pygame.font.SysFont(self.font, self.font_size)

        self.Hovering : bool = False
    def draw(self, screen):
        # Draw the Button Rect
        
        self.button_rect = pygame.draw.rect(screen, self.color, (self.world_position[0], self.world_position[1], self.width, self.height))
         # Draw the buttons label/text
        match self.text_align:
            case "Center":
                my_label = self.my_font.render(self.text, 1, self.text_color )
                text_rect = my_label.get_rect(center=(self.width/2, self.height/2))
                screen.blit(my_label, (text_rect.x, text_rect.y + (self.font_size/2))) # Middle        
            case "Left":
                my_label = self.my_font.render(self.text, 1, self.text_color)
                screen.blit(my_label, (self.world_position[0],self.world_position[1]))
            case "Right":
                my_label = self.my_font.render(self.text, 1, self.text_color)
                text_rect = my_label.get_rect(center=(self.width, self.height))
                screen.blit(my_label, (self.world_position[0] + (text_rect.x - text_rect.size[0]/2),self.world_position[1] + (text_rect.y -  text_rect.size[1]/2)))


    def _update_node(self, node, delta, the_input):
        if node.active:
            node.update(delta, the_input)
            for child in node.children:
                child._update_node(child, delta, the_input)

        self.check_button_actions(the_input)


    def check_button_actions(self, the_input):
        self.has_mouse_entered_button()

        self.is_button_pressed(the_input)

        self.has_mouse_exited_button()


    def has_mouse_entered_button(self):
        if self.button_rect == None or self.Hovering : return
        self.mouse = pygame.mouse.get_pos()

        if self.button_rect.collidepoint(self.mouse):
            self.Hovering = True
            print("Hovering over button")

    def has_mouse_exited_button(self):
        if self.button_rect == None or self.Hovering == False : return
        self.mouse = pygame.mouse.get_pos()

        if self.Hovering and not self.button_rect.collidepoint(self.mouse):
            self.Hovering = False
            print("Left button")

    def is_button_pressed(self, the_input):
        if self.button_rect == None or self.Hovering == False: return
        self.mouse = pygame.mouse.get_pos()

        if the_input.mouse_pressed_once(0):
            print("Clickad")
            #self.on_click.emit()