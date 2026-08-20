import pygame
pygame.init()
screen = pygame.display.set_mode((200,200))
screen.fill((255,255,255))
screen.set_at((100,100),(255,0,0))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()