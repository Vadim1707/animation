#Imports
import pygame, sys
from pygame.mouse import get_pos

#Constants
WIDTH, HEIGHT = 600, 589
RADIUS = 20
TITLE = "Smooth Movement"

#pygame initialization
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

#Player Class
class Game:
    def __init__(self, x, y, radius):
        # self.x = int(x)
        # self.y = int(y)
        # self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.rect = pygame.draw.circle(win, 'orange', (x, y), radius)
        self.color = (250, 120, 60)
        self.velX = 2
        self.velY = 3
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
        
    
    def draw(self, win):
        # pygame.draw.rect(win, self.color, self.rect)
        pygame.draw.circle(win, self.color, (self.rect.x, self.rect.y), self.rect.height)
    
    def update(self):
        # change of speed if on border
        if self.rect.x <= self.rect.height or self.rect.x >= WIDTH - self.rect.height:
            self.velX = -self.velX
        if self.rect.y <= self.rect.height or self.rect.y >= HEIGHT - self.rect.height:
            self.velY = -self.velY

        # stops if on coursor
        if self.coursor_on_circle():
            return
        
        # change of coordinates
        self.rect.x += self.velX
        self.rect.y += self.velY

        # prevents bug on edges
        if self.rect.x - self.rect.height < 0:
            self.rect.x += 2
        if self.rect.y - self.rect.height < 0:
            self.rect.y += 2  
        if self.rect.x - self.rect.height > WIDTH:
            self.rect.x -= 2
        if self.rect.y - self.rect.height > HEIGHT:
            self.rect.y -= 2  

    def coursor_on_circle(self) -> bool:
        x, y = get_pos()
        distance_from_center = ((x - self.rect.x)**2 + (y - self.rect.y)**2)**0.5
        return distance_from_center <= self.rect.height

#Player Initialization
player = Game(WIDTH/2, HEIGHT/2, RADIUS)

#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Draw
    win.fill((12, 24, 36))  
    player.draw(win)

    #update
    player.update()
    print(player.rect.x, player.rect.y, player.rect.x - player.rect.height,player.rect.y - player.rect.height)
    pygame.display.flip()

    clock.tick(120)