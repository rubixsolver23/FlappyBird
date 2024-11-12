import pygame
import sys
from game import Game



pygame.init()
screen = pygame.display.set_mode((400, 720))


mainClock = pygame.time.Clock()

SPAWNPIPE = pygame.USEREVENT

pygame.time.set_timer(SPAWNPIPE, 2500)

game = Game("img/bird.png", "img/pipe.png", "img/background.png", "img/ground.png")
game.resize_images()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.active:
                game.flap()
               
            elif event.key == pygame.K_SPACE and not game.active:
                game.restart()
        elif event.type == pygame.MOUSEBUTTONDOWN:
             if game.active:
                game.flap()

        elif event.type == SPAWNPIPE:
            game.spawn_pipe()

    

    game.show_background(screen)

    if game.active:
        game.show_bird(screen)
        game.update_bird()
        game.move_pipes()
        game.show_pipes(screen)
        game.check_collision()
        game.update_score()
        game.show_score("playing", screen, (255,255,255))
    else:
        game.game_over(screen, (0,0,0))



    game.show_ground(screen)
    game.move_ground()


    pygame.display.update()
    mainClock.tick(120)
