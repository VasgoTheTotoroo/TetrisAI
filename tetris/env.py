from .model import TetrisEngine
from .render import Rendering
import numpy as np


class TetrisEnv:
    
    def __init__(self, random_start=False):
        self.game = TetrisEngine(random_start)
        self.screen = None
        
    def seed(self, seed):
        self.game.seed(seed)
        
    def reset(self):
        self.game.clear()
        if self.screen: self.screen.init()
        state = self.game.state()
        return wrap_state(state)

    def step(self, action):
        state, reward, done = self.game.step(action)
        return wrap_state(state), reward, done
           
    def render(self, mode=None):
        if not self.screen:
            self.screen = Rendering(self.game)
            self.screen.init()
        frame = self.screen.render()
        return frame
               
    def close(self):
        if self.screen: 
            self.screen.render()
            self.screen.close()
            self.screen = None
            
    def __repr__(self):
        return str(self.game)


def wrap_state(state):
    grid, piece = state
    return Board(grid), Tetromino(piece)


class Board:
    
    def __init__(self, grid=np.zeros((10,20))):
        self.grid = np.array(grid).copy()
        
    def rows(self):
        return self.grid.shape[1]
    
    def columns(self):
        return self.grid.shape[0]
        
    def drop(self, tetromino, column=None):
        x_start = tetromino.anchor[0] if column is None else column 
        y_start = tetromino.anchor[1] if column is None else tetromino.start()
        piece = tetromino.move_to(x_start, y_start)
        if not self.can_place(piece):
            return None
        while True:
            down = piece.move_down()
            if self.can_place(down):
                piece = down
            else:
                return piece
        
    def can_place(self, tetromino):
        pos = tetromino.position()
        x,y = pos[:,0], pos[:,1]
        return np.all((pos >=0) & (pos < self.grid.shape)) and np.all(self.grid[x,y] == 0)
    
    def add(self, tetromino):
        new_board = Board(self.grid)
        new_board.grid[tetromino.coords()] = 1
        return new_board
        
    def __repr__(self):
        s = '   o' + '--' * self.grid.shape[0] + 'o\n'
        s += '\n'.join(["{:2d}".format(n) + ' |' + ''.join(['[]' if j else '  ' for j in i]) + '|' for n,i in enumerate(self.grid.T)])
        s += '\n   o' + '--' * self.grid.shape[0] + 'o'
        return s


class Tetromino:
    
    __tetro = {
        'T': [(0, 0), (-1,  0), ( 1,  0), ( 0, -1)],
        'J': [(0, 0), (-1,  0), ( 0, -1), ( 0, -2)],
        'L': [(0, 0), ( 1,  0), ( 0, -1), ( 0, -2)],
        'Z': [(0, 0), (-1,  0), ( 0, -1), ( 1, -1)],
        'S': [(0, 0), (-1, -1), ( 0, -1), ( 1,  0)],
        'I': [(0, 0), ( 0, -1), ( 0, -2), ( 0, -3)],
        'O': [(0, 0), ( 0, -1), (-1,  0), (-1, -1)],
    }
        
    @classmethod
    def create(cls, name, anchor=(0,0)):
        return Tetromino((anchor, cls.__tetro[name], name))
    
    def __init__(self, triplet):
        anchor, blocks, name = triplet
        self.anchor = np.array(anchor)
        self.blocks = np.array(blocks)
        self.name   = name
        
    def position(self):
        return self.blocks + self.anchor
    
    def coords(self):
        xy  = self.position()
        idx = (xy[:,0], xy[:,1])
        return idx
    
    def start(self):
        """Starting row of the tetromino, taking into account its height."""
        return -self.blocks[:,1].min()
    
    def move_to(self, x, y):
        return Tetromino(((x,y), self.blocks, self.name))
            
    def move_right(self):
        return Tetromino((self.anchor + (1,0), self.blocks, self.name))
    
    def move_left(self):
        return Tetromino((self.anchor - (1,0), self.blocks, self.name))

    def move_down(self):
        return Tetromino((self.anchor + (0,1), self.blocks, self.name))

    def rotate_right(self):
        return Tetromino((self.anchor, self.blocks[:,[1,0]] * (-1,1), self.name))
    
    def rotate_left(self):
        return Tetromino((self.anchor, self.blocks[:,[1,0]] * (1,-1), self.name))
    
    def action_for(self, landed):
        """Action that brings the tetromino 'self' closer to the tetromino 'landed' passed as input."""
        if landed is None: landed = self
        diff = landed.anchor[0] - self.anchor[0]
        move_left  = diff < 0
        move_right = diff > 0
        rotate_left  = np.all(landed.blocks == self.rotate_left().blocks)
        rotate_left |= np.all(landed.blocks == self.rotate_left().rotate_left().blocks)
        rotate_right = np.all(landed.blocks == self.rotate_right().blocks)
        rotate_right|= np.all(landed.blocks == self.rotate_right().rotate_right().blocks)
        if rotate_left:
            action = 3
        elif rotate_right:
            action = 4
        elif move_left:
            action = 1 
        elif move_right:
            action = 2
        else:  # drop down
            action = 5
        return action
        
    def __repr__(self):
        grid = np.zeros((10,20))
        pos  = self.position()
        x, y = pos[:,0], pos[:,1]
        grid[x,y] = 1
        s = '   o' + '--' * grid.shape[0] + 'o\n'
        s += '\n'.join(["{:2d}".format(n) + ' |' + ''.join(['[]' if j else '  ' for j in i]) + '|' for n,i in enumerate(grid.T)])
        s += '\n   o' + '--' * grid.shape[0] + 'o'
        return s

