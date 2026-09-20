import pygame

pygame.init()

screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("car game")

icon = pygame.image.load("car.png")
pygame.display.set_icon(icon)

car = pygame.image.load("car.png")
bgimg = pygame.image.load("racetrack.png")
small_car = pygame.transform.scale(car,(80,80))


x = 230
y = 120

def player(x,y):
    screen.blit(small_car,(x,y))

running = True

while running:
    screen.fill((0,0,0))
    screen.blit(bgimg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player(x,y)
    pygame.display.update()
