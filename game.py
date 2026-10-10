import pygame
import time

pygame.init()
WIDTH = 600
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Happy Birthday card')

bg1 = pygame.image.load('bg1.jpg')
bg1 = pygame.transform.scale(bg1, (WIDTH,HEIGHT))

running = True
while running:
    #first screen
    font1 = pygame.font.SysFont('Calibri', 40)
    text1 = font1.render('Happy birthday to you!!! ', True, '#D32116')
    text1_rect = text1.get_rect(center = (CENTER_X,CENTER_Y - 50))
    SCREEN.fill((255,255,255))
    SCREEN.blit(bg1, (0,0))
    SCREEN.blit(text1, text1_rect)
    pygame.display.update()
    time.sleep(3)

    #second screen
    bg2 = pygame.image.load('bg2.jpg')
    bg2 = pygame.transform.scale(bg2, (WIDTH,HEIGHT))
    font2 = pygame.font.SysFont('Verdana', 30)
    text2 = font2.render('Have a great day!!', True, '#2130BB' )
    text2_rect = text2.get_rect(center = (CENTER_X, CENTER_Y - 50))
    





pygame.quit()