import pygame
import Values.constants as const

class graphic:
    def __init__(self):
        self.screen = pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))
        pygame.display.set_caption(const.WINDOW_TITLE)
        self.screen.fill(const.BOARD_COLOR)
        pygame.display.update()
    
    def draw_X(self, x, y):
        #    x
        # y ╔═════════════════════════════════▶
        #   ║ (X1, Y1) ╔═══╗ (X2, Y1)
        #   ║          ║   ║
        #   ▼ (X1, Y2) ╚═══╝ (X2, Y2)
        #
        # line 1: (X1, Y1) -> (X2, Y2)
        # line 2: (X1, Y2) -> (X2, Y1)
        pos_X1 = const.BORDER_SIZE + x * const.SQUARE_SIZE
        pos_X2 = const.BORDER_SIZE + (x+1) * const.SQUARE_SIZE
        pos_Y1 = const.BORDER_SIZE + y * const.SQUARE_SIZE
        pos_Y2 = const.BORDER_SIZE + (y+1) * const.SQUARE_SIZE
        # subtract cell border
        pos_X1 = pos_X1 + const.CELL_BORDER
        pos_X2 = pos_X2 - const.CELL_BORDER
        pos_Y1 = pos_Y1 + const.CELL_BORDER
        pos_Y2 = pos_Y2 - const.CELL_BORDER
        # draw line 1
        pygame.draw.line(self.screen, const.COLOR_BLUE, (pos_X1, pos_Y1), (pos_X2, pos_Y2), const.X_LINE_THICKNESS)
        # draw line 2
        pygame.draw.line(self.screen, const.COLOR_BLUE, (pos_X1, pos_Y2), (pos_X2, pos_Y1), const.X_LINE_THICKNESS)
        
    def draw_O(self, x, y):
        posX = const.BORDER_SIZE + const.SQUARE_SIZE/2 + x * const.SQUARE_SIZE
        posY = const.BORDER_SIZE + const.SQUARE_SIZE/2 + y * const.SQUARE_SIZE
        # draw circle (already subtracted cell border in O_RADIUS)
        pygame.draw.circle(self.screen, const.COLOR_RED, [posX, posY], const.O_RADIUS , const.O_LINE_THICKNESS)
    
    def draw_board(self, board):
        # draw board
        for i in range (0, const.COLS + 1):
            # draw vertical line
            pygame.draw.line(self.screen, const.COLOR_BLACK, 
            [const.BORDER_SIZE + const.SQUARE_SIZE * i, const.BORDER_SIZE], [const.BORDER_SIZE + const.SQUARE_SIZE * i, const.BOARD_HEIGHT + const.BORDER_SIZE], const.LINE_WIDTH)
            # draw horizontal line
            pygame.draw.line(self.screen, const.COLOR_BLACK,
            [const.BORDER_SIZE, const.BORDER_SIZE + const.SQUARE_SIZE * i], [const.BOARD_WIDTH + const.BORDER_SIZE, const.BORDER_SIZE + const.SQUARE_SIZE * i], const.LINE_WIDTH)
        
        for i in range (0, const.ROWS):
            for j in range (0, const.COLS):
                # 1: X
                if board[i][j] == 1: 
                    self.draw_X(i, j)
                # 2: O
                if board[i][j] == 2: 
                    self.draw_O(i, j)
        pygame.display.update()




        

