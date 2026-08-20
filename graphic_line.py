import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))
screen.fill((255, 255, 255))

x1, y1 = 10, 10
x2, y2 = 100, 180

m = (y2 - y1) / (x2 - x1)
c = y1 - m * x1

if m > 1:
    for y in range(y1, y2 + 1):
        x = (y - c) / m
        screen.set_at((round(x), y), (255, 0, 0))

else:
    for x in range(x1, x2 + 1):
        y = m * x + c
        screen.set_at((x, round(y)), (255, 0, 0))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()