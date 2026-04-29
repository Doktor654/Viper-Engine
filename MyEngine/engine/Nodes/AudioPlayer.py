import pygame
from engine.Node import Node
from engine.Core.Signal import Signal

class AudioPlayer(Node):
    def __init__(self, parent, children=[], name="AudioPlayer", active=True, audio_file="", volume=0.5, loop=False):
        super().__init__(parent, children, name, active)
        
        self.audio_file = audio_file
        self.volume = volume
        self.loop = loop

        self.is_playing = False
        self.finished_playing = Signal()
        self.finished_playing.connect(self.on_finish)

        self.mixer = pygame.mixer
        self.mixer.init()
        print("Path ", self.audio_file)
        self.sound = self.mixer.Sound(self.audio_file)
        self.sound.set_volume(self.volume)
        #self.sound.set_loop(self.loop)
    
    def play_audio(self):
        self.sound.play()
        self.is_playing = True
        
    def stop_audio(self):
        self.sound.stop()
        self.is_playing = False
    
    def update(self, delta, the_input):
        super().update(delta, the_input)
    
        if pygame.mixer.Channel(0).get_busy() == False and self.is_playing:
            self.finished_playing.emit()

    def on_finish(self):
        if self.loop and pygame.mixer.Channel(0).get_busy() == False:
            self.play_audio()
    