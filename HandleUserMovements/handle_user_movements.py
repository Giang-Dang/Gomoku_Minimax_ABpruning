import math
import Values.constants as const

class HandleUserMovements:
    def is_MousePos_In_Board(self, mousePos):
        mousePosX, mousePosY = mousePos
        if const.BOARD_POS_X_MIN < mousePosX < const.BOARD_POS_X_MAX and const.BOARD_POS_Y_MIN < mousePosY < const.BOARD_POS_Y_MAX:
            return True
        return False

    def convert_MousePos_To_BoardCoordinate(self, mousePos):
        mousePosX, mousePosY = mousePos
        print(mousePosX, mousePosY)
        Board_Y = math.floor((mousePosX - const.BOARD_POS_X_MIN) / const.SQUARE_SIZE)
        Board_X = math.floor((mousePosY - const.BOARD_POS_Y_MIN) / const.SQUARE_SIZE)
        return (Board_X, Board_Y)

    def checkValidMove(self, mousePos, board):
        x, y = self.convert_MousePos_To_BoardCoordinate(mousePos)
        if (board[x][y] == 0):
            print("true", x, y)
            return True
        print("false", x, y)
        return False

    def updateBoard_From_MousePos(self, mousePos, board, playerMoves):
        x, y = self.convert_MousePos_To_BoardCoordinate(mousePos)
        print(x, y)
        playerMoves.append((x, y))
        board[x][y] = 1
