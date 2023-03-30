from operator import truediv
import pygame

pygame.init()


screen = pygame.display.set_mode([800, 800])

x = True

while x:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

pygame.quit()
