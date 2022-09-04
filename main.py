import pygame
import Graphics.graphic as graphic
import Values.constants as const
import HandleUserMovements.handle_user_movements as mov

FPS = 60
BOARD = []
PLAYER_MOVES = []
COM_MOVES = []
TESTBOARD = [
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

def main():
    pygame.init()
    pygame.font.init()

    WIN = graphic.graphic()
    BOARD = const.NEW_BOARD.copy()

    # test
    BOARD = TESTBOARD.copy()

    WIN.draw_board(BOARD, "PRESS \"NEW GAME\" TO START NEW GAME", const.COLOR_BLUE)

    handleMoves = mov.HandleUserMovements()

    isPlayOrder = False
    isPlayerTurn = True

    run = True
    clock = pygame.time.Clock()    
    while run:
        clock.tick(FPS)

        # MOUSE BUTTON DOWN
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_Pos = pygame.mouse.get_pos()
            mouse_posX, mouse_posY = mouse_Pos

            # mouse postion in NEW GAME BUTTON
            if const.NEW_GAME_BUTTON_POS_X_MIN < mouse_posX < const.NEW_GAME_BUTTON_POS_X_MAX and const.NEW_GAME_BUTTON_POS_Y_MIN < mouse_posY < const.NEW_GAME_BUTTON_POS_Y_MAX:
                
                BOARD = [row[:] for row in const.NEW_BOARD]


                WIN.clear()
                WIN.draw_board(BOARD, "PLAYER TURN", const.COLOR_BLUE)
                isPlayerTurn = True
                isPlayOrder = True
            if isPlayOrder:
                # Player Turn
                if isPlayerTurn and handleMoves.is_MousePos_In_Board(mouse_Pos):
                    if handleMoves.checkValidMove(mouse_Pos, BOARD):
                        handleMoves.updateBoard_From_MousePos(mouse_Pos, BOARD, PLAYER_MOVES)
                        WIN.clear()
                        WIN.draw_board(BOARD, "COMPUTER TURN", const.COLOR_RED)
                        isPlayerTurn = False

                # Computer Turn
                if not isPlayerTurn:
                    cal_NextMove_MiniMax(BOARD, COM_MOVES)
                    WIN.clear()
                    WIN.draw_board(BOARD, "PLAYER TURN", const.COLOR_BLUE)
                    isPlayerTurn = True



        # QUIT
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()


