import random
import sys,pygame


def axes():
    xas = random.randint(0,400)
    return xas



game_state = True
size = widht, height = 400,400
screen = pygame.display.set_mode(size)
black = 0,0,0
white = 255,255,255


while game_state:
    for events in pygame.event.get():
        if events.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    for i in range(0,20):
        pygame.draw.rect(screen,white,(axes(),axes(),5,5))
    pygame.display.flip()