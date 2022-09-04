from pickle import FALSE
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
        pos_X1 = const.BOARD_POS_X_MIN + y * const.SQUARE_SIZE
        pos_X2 = const.BOARD_POS_X_MIN + (y+1) * const.SQUARE_SIZE
        pos_Y1 = const.BOARD_POS_Y_MIN + x * const.SQUARE_SIZE
        pos_Y2 = const.BOARD_POS_Y_MIN + (x+1) * const.SQUARE_SIZE
        # subtract cell border
        pos_X1 = pos_X1 + const.X_CELL_BORDER
        pos_X2 = pos_X2 - const.X_CELL_BORDER
        pos_Y1 = pos_Y1 + const.X_CELL_BORDER
        pos_Y2 = pos_Y2 - const.X_CELL_BORDER
        # draw line 1
        pygame.draw.line(self.screen, const.COLOR_BLUE, (pos_X1, pos_Y1), (pos_X2, pos_Y2), const.X_LINE_THICKNESS)
        # draw line 2
        pygame.draw.line(self.screen, const.COLOR_BLUE, (pos_X1, pos_Y2), (pos_X2, pos_Y1), const.X_LINE_THICKNESS)
        
    def draw_O(self, x, y):
        posX = const.BOARD_POS_X_MIN + const.SQUARE_SIZE/2 + y * const.SQUARE_SIZE + const.O_LINE_THICKNESS/2
        posY = const.BOARD_POS_Y_MIN + const.SQUARE_SIZE/2 + x * const.SQUARE_SIZE + const.O_LINE_THICKNESS/2
        # subtract cell border
        radius = const.O_RADIUS - const.O_CELL_BORDER
        # draw circle
        pygame.draw.circle(self.screen, const.COLOR_RED, [posX, posY], radius , const.O_LINE_THICKNESS)
    
    def draw_button(self, pos, width, height, text):
        rectButton = pygame.Rect(pos, (width, height))
        font_text = pygame.font.Font(pygame.font.get_default_font(), const.BUTTON_TEXT_FONT_SIZE)
        text_surf = font_text.render(text, True, const.BUTTON_TEXT_COLOR)
        text_rect = text_surf.get_rect(center = rectButton.center)
        pygame.draw.rect(self.screen, const.BUTTON_COLOR, rectButton)
        self.screen.blit(text_surf, text_rect)

    def draw_info_text(self, text, textColor):
        text_pos = (const.WINDOW_WIDTH/2, const.BORDER_SIZE + const.INFO_TEXT_FONT_SIZE/2)

        font_text = pygame.font.Font(pygame.font.get_default_font(), const.INFO_TEXT_FONT_SIZE)
        text_surf = font_text.render(text, False, textColor)
        text_rect = text_surf.get_rect(center = text_pos)
        self.screen.blit(text_surf, text_rect)
        pygame.display.update()

    
    def draw_board(self, board, infoText, infoTextColor):
        # draw board
        for i in range (0, const.BOARD_COLS + 1):
            # draw vertical line
            pygame.draw.line(self.screen, const.COLOR_BLACK, 
            [const.BOARD_POS_X_MIN + const.SQUARE_SIZE * i, const.BOARD_POS_Y_MIN], [const.BOARD_POS_X_MIN + const.SQUARE_SIZE * i, const.BOARD_POS_Y_MIN + const.BOARD_HEIGHT], const.BOARD_LINE_WIDTH)
            # draw horizontal line
            pygame.draw.line(self.screen, const.COLOR_BLACK,
            [const.BOARD_POS_X_MIN, const.BOARD_POS_Y_MIN + const.SQUARE_SIZE * i], [const.BOARD_POS_X_MIN + const.BOARD_WIDTH, const.BOARD_POS_Y_MIN + const.SQUARE_SIZE * i], const.BOARD_LINE_WIDTH)
        
        # draw INFO TEXT
        self.draw_info_text(infoText, infoTextColor)

        # draw NEW GAME button
        self.draw_button(const.NEW_GAME_BUTTON_POS, const.BUTTON_WIDTH, const.BUTTON_HEIGHT, "NEW GAME")

        # test
        print(board)

        # render board moves
        for i in range (0, const.BOARD_ROWS):
            for j in range (0, const.BOARD_COLS):
                # 1: O
                if board[i][j] == 1: 
                    self.draw_O(i, j)
                # 2: X
                if board[i][j] == 2: 
                    self.draw_X(i, j)

        pygame.display.update()
    
    def clear(self):
        self.screen.fill(const.BOARD_COLOR)
        pygame.display.update()




        

