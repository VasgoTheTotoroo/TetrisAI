import pygame
import pygame.locals
import numpy as np

FPS = 10
SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480

BOARD_WIDTH = 10
BOARD_HEIGHT = 20

BOXSIZE = 20
XMARGIN = (SCREEN_WIDTH - BOARD_WIDTH * BOXSIZE) // 2
TOPMARGIN = SCREEN_HEIGHT - (BOARD_HEIGHT * BOXSIZE) - 5

#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)
CYAN        = (  0, 155, 155)
LIGHTCYAN   = ( 20, 175, 175)
MAGENTA     = (155,   0, 155)
LIGHTMAGENTA= (175,   0, 175)
ORANGE      = (255, 140,   0)
LIGHTORANGE = (255, 165,   0)


COLORS      = (     BLUE,      GREEN,      RED,      YELLOW,      CYAN,      MAGENTA,      ORANGE)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW, LIGHTCYAN, LIGHTMAGENTA, LIGHTORANGE)



class Rendering:
    
    def __init__(self, model):
        self.model = model
        pygame.display.init()
        self.clock = pygame.time.Clock()
        
    def init(self):
        self.quit = False
        self._display()
        self.render()
        
    def render(self):
        self._process_events()
        self._draw_background()
        self._draw_board()
        pygame.display.flip()
        self.clock.tick(FPS)
        return self._screenshot()
        
    def close(self):
        pygame.display.quit()
        
    def _draw_background(self):
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, WHITE, (XMARGIN-3, TOPMARGIN-7, (BOARD_WIDTH*BOXSIZE)+8, (BOARD_HEIGHT*BOXSIZE)+10), 5)
    
    def _draw_board(self):
        self.model._set_piece(True)
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_HEIGHT):
                self._draw_box(x, y, self.model.board[x,y])
        self.model._set_piece(False)
        
    def _draw_box(self, x, y, piece):
        if piece > 0:
            i = int(piece-1)
            pixelx, pixely = (XMARGIN + (x * BOXSIZE)), (TOPMARGIN + (y * BOXSIZE))
            pygame.draw.rect(self.screen, COLORS[i], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
            pygame.draw.rect(self.screen, LIGHTCOLORS[i], (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))
        
    #-----#
    
    def _display(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        
    def _screenshot(self):
        img = pygame.surfarray.array3d(pygame.display.get_surface()).astype(np.uint8)
        return np.fliplr(np.rot90(img,3))
        
    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True    
        keys = pygame.key.get_pressed()
        self.action = 0
        if keys[pygame.locals.K_LEFT]:
            self.action = 1
        elif keys[pygame.locals.K_RIGHT]:
            self.action = 2
        elif keys[pygame.locals.K_UP]:
            self.action = 3
        elif keys[pygame.locals.K_DOWN]:
            self.action = 5            
