import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
font= pygame.font.Font(r'C:\Users\Mitko\Desktop\python2023\homework\GameProject\Pixeltype.ttf',70)

surface = pygame.image.load(r'C:\Users\Mitko\Desktop\python2023\homework\GameProject\blue.jpeg').convert()
grass = pygame.image.load(r'C:\Users\Mitko\Desktop\python2023\homework\GameProject\gr.jpg').convert_alpha()
test_font = font.render('Igrata mi ',False,'#3d7724').convert()
cat = pygame.image.load(r'C:\Users\Mitko\Desktop\python2023\homework\GameProject\cat.jpg').convert_alpha()
cat_posicion = 600

player = pygame.image.load(r'C:\Users\Mitko\Desktop\python2023\homework\GameProject\pln.png').convert_alpha()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(surface,(0,0))
    screen.blit(grass,(0,350))

    screen.blit(test_font,(300,50))
    cat_posicion -= 5
    if cat_posicion < -100: cat_posicion = 800
    screen.blit(cat,(cat_posicion,250))
    screen.blit(player,(80,258))

    pygame.display.update()        
    clock.tick(60)