import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
font= pygame.font.Font(r'C:\Users\Mitko\Desktop\python2023\homework\GameProject\Pixeltype.ttf',70)

surface = pygame.image.load(r'C:\Users\Mitko\Desktop\python2023\homework\GameProject\blue.jpeg')
grass = pygame.image.load(r'C:\Users\Mitko\Desktop\python2023\homework\GameProject\grd.png')
test_font = font.render('Igrata mi ',False,'#3d7724')
cat = pygame.image.load(r'C:\Users\Mitko\Desktop\python2023\homework\GameProject\cat.jpg')
cat_posicion = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(surface,(0,0))
    screen.blit(grass,(0,100))
    screen.blit(grass,(400,100))
    screen.blit(test_font,(300,50))
    cat_posicion -= 5
    if cat_posicion < -100: cat_posicion = 800
    screen.blit(cat,(cat_posicion,150))

    pygame.display.update()        
    clock.tick(60)