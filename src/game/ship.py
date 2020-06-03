import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.transform.scale(pygame.image.load("./images/ship.bmp"), (50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def blitem(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx += 50
        if self.moving_left:
            self.rect.centerx -= 50

