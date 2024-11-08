import pygame
import sys
from game import Game



pygame.init()
screen = pygame.display.set_mode((400, 720))


mainClock = pygame.time.Clock()
game = Game("img/bird.png", "img/pipe.png", "img/background.png", "img/ground.png")
game.resize_images()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.show_background(screen)

    
    pygame.display.update()
    mainClock.tick(120)
