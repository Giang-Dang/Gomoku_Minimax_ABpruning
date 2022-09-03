import pygame
import Graphics.graphic as graphic
import Values.constants as const

FPS = 60
BOARD = []

def main():

    WIN = graphic.graphic()

    run = True
    clock = pygame.time.Clock()    
    while run:
        clock.tick(FPS)
        WIN.draw_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()


