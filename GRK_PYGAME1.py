import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")
poly_surface = pygame.Surface((300, 300))

x = y = r = 150
angles_count = 9

poly_points = []
i = 0
while i < 9:
    poly_points.append( (x - math.cos(i * (2 * math.pi / angles_count)) * r,
                      y - math.sin(i * (2 * math.pi / angles_count)) * r) )
    i += 1
pygame.draw.polygon(poly_surface, (127,127,255), poly_points)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                win.fill((0,0,0))
                pygame.display.update()
                win.blit(poly_surface, (150,150))
            elif event.key == pygame.K_2:
                win.fill((0, 0, 0))
                pygame.display.update()
                transformed_surface = pygame.transform.scale(poly_surface, (500, 500))
                transformed_surface = pygame.transform.rotate(transformed_surface, -45)
                win.blit(transformed_surface,
                         (-(transformed_surface.get_width()/2)+300,-(transformed_surface.get_height()/2)+300))
            elif event.key == pygame.K_3:
                win.fill((0, 0, 0))
                pygame.display.update()
                transformed_surface = pygame.transform.scale(poly_surface, (300, 500))
                transformed_surface = pygame.transform.rotate(transformed_surface, -180)
                win.blit(transformed_surface,
                         (-(transformed_surface.get_width() / 2) + 300, -(transformed_surface.get_height() / 2) + 300))
            elif event.key == pygame.K_4:
                win.fill((0, 0, 0))
                pygame.display.update()
                transformed_surface = pygame.transform.scale(poly_surface, (300, 500))
                transformed_surface = pygame.transform.rotate(transformed_surface, 30)
                transformed_surface = pygame.transform.scale(transformed_surface, (300, 300))
                win.blit(transformed_surface,
                         (-(transformed_surface.get_width() / 2) + 300, -(transformed_surface.get_height() / 2) + 300))
            elif event.key == pygame.K_5:
                win.fill((0, 0, 0))
                pygame.display.update()
                transformed_surface = pygame.transform.scale(poly_surface, (300, 150))
                win.blit(transformed_surface,
                         (-(transformed_surface.get_width() / 2) + 300, 0))
            elif event.key == pygame.K_6:
                win.fill((0, 0, 0))
                pygame.display.update()
                transformed_surface = pygame.transform.scale(poly_surface, (300, 500))
                transformed_surface = pygame.transform.rotate(transformed_surface, 30)
                transformed_surface = pygame.transform.scale(transformed_surface, (300, 300))
                transformed_surface = pygame.transform.rotate(transformed_surface, -90)
                win.blit(transformed_surface,
                         (-(transformed_surface.get_width() / 2) + 300, -(transformed_surface.get_height() / 2) + 300))
            elif event.key == pygame.K_7:
                win.fill((0, 0, 0))
                pygame.display.update()
                transformed_surface = pygame.transform.scale(poly_surface, (300, 500))
                transformed_surface = pygame.transform.rotate(transformed_surface, -180)
                transformed_surface = pygame.transform.flip(transformed_surface, True, False)
                win.blit(transformed_surface,
                         (-(transformed_surface.get_width() / 2) + 300, -(transformed_surface.get_height() / 2) + 300))

            elif event.key == pygame.K_8:
                win.fill((0, 0, 0))
                pygame.display.update()
                transformed_surface = pygame.transform.scale(poly_surface, (300, 150))
                transformed_surface = pygame.transform.rotate(transformed_surface, -30)
                win.blit(transformed_surface,
                         (50, 300))

            elif event.key == pygame.K_9:
                win.fill((0, 0, 0))
                pygame.display.update()
                transformed_surface = pygame.transform.scale(poly_surface, (300, 500))
                transformed_surface = pygame.transform.rotate(transformed_surface, 30)
                transformed_surface = pygame.transform.scale(transformed_surface, (300, 300))
                transformed_surface = pygame.transform.rotate(transformed_surface, -180)
                win.blit(transformed_surface,
                         (600-(transformed_surface.get_width()), -(transformed_surface.get_height() / 2) + 300))

    pygame.display.update()
