import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")
win.fill((255, 255, 255))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.circle(win, (0, 0, 0), (300, 300), 150)
    pygame.draw.rect(win, (255, 255, 0), (225, 225, 150, 150))
    pygame.display.update()