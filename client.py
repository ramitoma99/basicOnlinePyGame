import pygame

width = 500
height = 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

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

def redrawWindow(window, player):
    window.fill((255, 255, 255))
    player.draw(window)
    pygame.display.update()

def main():
    run = True
    p = Player(50, 50, 100, 100, (0,255,0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        p.move()
        redrawWindow(window, p)

main()