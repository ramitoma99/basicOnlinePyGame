import pygame
from network import Network

width = 500
height = 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3
    
    def draw(self, win):
        pygame.draw.rect(window, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)

def read_pos(str):
    str = str.split(",")
    return int(str[0], int(str[1]))

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redrawWindow(window, player):
    window.fill((255, 255, 255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()

def main():
    run = True
    p = Player(50, 50, 100, 100, (0,255,0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)

        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        p.move()
        redrawWindow(window, p, p2)

main()