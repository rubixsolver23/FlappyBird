import pygame
import sys
from game import Game



pygame.init()
screen = pygame.display.set_mode((400, 720))


mainClock = pygame.time.Clock()

SPAWNPIPE = pygame.USEREVENT
#INCREASESPEED = pygame.USEREVENT

pygame.time.set_timer(SPAWNPIPE, 2500)
#pygame.time.set_timer(INCREASESPEED, 1000)

game = Game("img/bird.png", "img/pipe.png", "img/background.png", "img/ground.png")
game.resize_images()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.active:
                   game.flap()
        if event.type == pygame.MOUSEBUTTONDOWN:
             if game.active:
                game.flap()
        if event.type == SPAWNPIPE:
            game.spawn_pipe()

        #if event.type == INCREASESPEED:
         #   game.game_speed += 0.1


    

    game.show_background(screen)

    if game.active:
        game.show_bird(screen)
        game.update_bird()
        game.move_pipes()
        game.show_pipes(screen)
        game.check_collision()



    game.show_ground(screen)
    game.move_ground()


    pygame.display.update()
    mainClock.tick(120)
