import pygame
import random

class Game:
    def __init__(self, bird_img, pipe_img, background_img, ground_img):
        self.bird = pygame.image.load(bird_img).convert_alpha()
        self.bird_rect = self.bird.get_rect(center = (70,180))
        self.pipe = pygame.image.load(pipe_img).convert_alpha()
        self.background = pygame.image.load(background_img).convert_alpha()
        self.ground = pygame.image.load(ground_img).convert_alpha()
        self.ground_position = 0
        self.active = True
        self.gravity = 0.05
        self.bird_movement = 0
        self.rotated_bird = pygame.Surface((0,0))
        self.pipes = []
        self.pipe_height = [280, 425, 562]
        self.game_speed = 1
        self.score = 0
        self.font = pygame.font.SysFont(None, 48)
        self.high_score = 0
    
    def resize_images(self):
        self.bird = pygame.transform.scale(self.bird, (51,34))
        self.pipe = pygame.transform.scale(self.pipe, (80,438))
        self.background = pygame.transform.scale(self.background, (400,720))
        self.ground = pygame.transform.scale(self.ground, (470,160))

    def show_background(self, screen):
        screen.blit(self.background, (0,0))

    def show_ground(self, screen):
        screen.blit(self.ground, (self.ground_position, 650))

    def move_ground(self):
        self.ground_position -= self.game_speed
        self.ground_position %= 43.5
        self.ground_position -= 43.5
    
    def show_bird(self, screen):
        screen.blit(self.rotated_bird, self.bird_rect)

    def update_bird(self):
        self.bird_movement += self.gravity
        self.rotated_bird = self.rotate_bird()
        self.bird_rect.centery += self.bird_movement

    def rotate_bird(self):
        new_bird = pygame.transform.rotozoom(self.bird, -self.bird_movement * 4, 1)
        return new_bird

    def flap(self):
        self.bird_movement = -3

    def spawn_pipe(self):
        random_pipe_pos = random.choice(self.pipe_height)
        bottom_pipe = self.pipe.get_rect(midtop = (600,random_pipe_pos))
        top_pipe = self.pipe.get_rect(midbottom = (600, random_pipe_pos-200))
        self.pipes.append(bottom_pipe)
        self.pipes.append(top_pipe)

    def move_pipes(self):
        for pipe in self.pipes:
            pipe.right -= self.game_speed
            if pipe.right <= 0:
                self.pipes.remove(pipe)
    
    def show_pipes(self, screen):
        for pipe in self.pipes:
            if pipe.bottom >= 700:
                screen.blit(self.pipe, pipe)
            else:
                flip_pipe = pygame.transform.flip(self.pipe, False, True)
                screen.blit(flip_pipe, pipe)

    def check_collision(self):
        self.active = self.bird_rect.collidelist(self.pipes) < 0
        
        if self.bird_rect.top <= -100 or self.bird_rect.bottom >= 650:
            self.active = False

    def update_score(self):
        self.score += 0.01
        self.score = round(self.score, 2)

    def show_score(self, game_state, screen, color):
        score_surface = self.font.render(str(int(self.score)), True, color)
        score_rect = score_surface.get_rect(center=(202,75))
        screen.blit(score_surface, score_rect)

        if game_state == "game_over":
            restart_text1 = self.font.render("Press Space Bar", True, color)
            restart_rect1 = restart_text1.get_rect(center=(200,280))
            screen.blit(restart_text1, restart_rect1)

            restart_text2 = self.font.render("to Play Again", True, color)
            restart_rect2 = restart_text2.get_rect(center=(200,340))
            screen.blit(restart_text2, restart_rect2)

            high_score_surface = self.font.render("High Score: {:d}".format(int(self.high_score)), True, color)
            high_score_rect = high_score_surface.get_rect(center=(200, 400))
            screen.blit(high_score_surface, high_score_rect)

    def game_over(self, screen, color):
        self.update_high_score()
        self.show_score("game_over", screen, color)
        

    def update_high_score(self):
        if self.high_score < self.score:
            self.high_score = self.score
    
    def restart(self):
        self.active = True
        del self.pipes[:]
        self.bird_rect.center = (70, 180)
        self.bird_movement = 0
        self.score = 0

