import pygame
import sys

pygame.init()

# screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and icon
pygame.display.set_caption("Buttle")

# images
player = pygame.image.load('./images/spaceship.png')


# Player
class Player:
    def __init__(self):
        self.playerImg = pygame.transform.scale(player, (80, 80))
        self.playerX = 360
        self.playerY = 460
        self.lBounary = 100
        self.rBounary = 700

    def playerDraw(self):
        screen.blit(self.playerImg, (self.playerX, self.playerY))

    def playerMove(self):
        key = pygame.key.get_pressed()
        if self.playerX > 700:
            self.playerX = 700
        elif self.playerX < 100:
            self.playerX = 100
        elif key[pygame.K_d]:
            self.playerX += 0.1
        elif key[pygame.K_a]:
            self.playerX -= 0.1



player = Player()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.K_d:
            print('fefe')

    screen.fill((0, 0, 255))

    player.playerDraw()
    player.playerMove()
    pygame.display.flip()
