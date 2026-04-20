from engine.Core.Signal import Signal
from engine.Node import Node

class TimerNode(Node):
    def __init__(self, parent, children=[], name="Timer", active=True, start_time=1, autostart=True, oneshot=False):
        super().__init__(parent, children, name, active)
        self.start_time = start_time
        self.oneshot = oneshot
        self.count_down = start_time
        self.running = autostart

        self.timer_done = Signal()

    def start_timer(self, duration=None):
        self.count_down = duration or self.start_time
        self.running = True

    def _update_node(self, node, delta, the_input):
        if not self.running:
            return
        
        self.count_down -= delta

        if self.count_down <= 0:
            self.running = False
            self.timer_done.emit()
            if not self.oneshot:
                self.start_timer()