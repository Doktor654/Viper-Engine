import pygame

class Signal:
    def __init__(self):
        self.listeners = []
    def connect(self, func):
        self.listeners.append(func)
    def emit(self, *args):
        for func in self.listeners:
            func(*args)