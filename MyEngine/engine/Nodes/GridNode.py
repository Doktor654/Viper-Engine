import pygame
from engine.Nodes.TransformNode import TransformNode

class GridNode(TransformNode):
    def __init__(self, parent, children=[], name="GridNode", active=True, cell_size=[16, 16], columns=16, rows=16, debug=False):
        super().__init__(parent, children, name, active)

        self.cell_size = cell_size
        self.columns = columns
        self.rows = rows
        self._cells : dict = {}
        self.debug = debug

        self.create_cells()
        

        
    def create_grid_Rect(self, column, row):
        # Create Grid Rect Size
        # Left, Right, Width, Height
        return [
            column * self.cell_size[0],
            row * self.cell_size[1],
            self.cell_size[0],
            self.cell_size[1]
        ]
    def create_cells(self):
        for column in range(self.columns):
            for row in range(self.rows):
                self._cells[column, row] = None

    def create_grid(self, screen):
        for cell in self._cells:
            grid_rect = self.create_grid_Rect(cell[0], cell[1])
            if self.debug:
                
                rect = pygame.Rect(grid_rect)
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)
    
    def update(self, delta, input):
        return super().update(delta, input)
    
    def draw(self, screen, offset=...):
        self.create_grid(screen)
        
        return super().draw(screen, offset)
    
    def get_world_position(self, x,y):
        col = int(x // self.cell_size[0])
        row = int(y // self.cell_size[1])

        return (col, row)
    def get_cell_to_world_position(self, x,y):
        pos_x = x * self.cell_size[0]
        pos_y = y * self.cell_size[1]

        return (pos_x, pos_y)
    def set_cell(self, col, row, data):
        self._cells[(col,row)] = data
    def get_cell_data(self, col, row):
        if self.is_cell_valid(col, row):
            return self._cells[col,row]
        return None
    def clear_cell(self, col,row):
        self._cells[(col,row)] = None
    def is_occupied(self, col, row):
        if self._cells[(col, row)] != None:
            return True
        return False
    def get_occupied_cells(self):
        occupied_cells = []
        for cell in self._cells.keys():
            if self.is_occupied(cell[0], cell[1]):
                occupied_cells.append(cell)
        return occupied_cells
    def is_cell_valid(self, col,row):
        if (col,row) in self._cells:
            return True

        return False