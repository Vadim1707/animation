#Imports
import pygame, sys
from pygame.mouse import get_pos, get_pressed

#Constants
WIDTH, HEIGHT = 600, 589
RADIUS = 60
TITLE = "Smooth Movement"

#pygame initialization
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

class Game:
    def __init__(self, x, y, radius):
        self.rect = pygame.draw.circle(win, 'orange', (x, y), radius)
        self.color = (250, 120, 60)
        self.velX = 2
        self.velY = 3
        
    
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
        if self.circle_clicked():
            return
        
        # change of coordinates
        self.rect.x += self.velX
        self.rect.y += self.velY

        # prevents bug on edges
        # woah, that took a while
        if self.rect.x < self.rect.height + self.velX:
            self.rect.x += abs(self.velX)
            
        if self.rect.y < self.rect.height + self.velY:
            self.rect.y += abs(self.velY)
            
        if self.rect.x > WIDTH - self.rect.height + self.velX:
            self.rect.x -= abs(self.velX)
            
        if self.rect.y > HEIGHT - self.rect.height + self.velY:
            self.rect.y -= abs(self.velY)
        
    
    def circle_clicked(self) -> bool:
        x, y = get_pos()
        left_click, *_ = get_pressed()
        distance_from_center = ((x - self.rect.x)**2 + (y - self.rect.y)**2)**0.5
        return distance_from_center <= self.rect.height and left_click 
    
    def distance_to_circle(self) -> float:
        # negative if inside circle
        # positive if outside
        x, y = get_pos()
        distance_from_center = ((x - self.rect.x)**2 + (y - self.rect.y)**2)**0.5
        distance_to_border = distance_from_center - self.rect.height
        return distance_to_border
    
    def change_speed(self):
        pass
    def next_frame(self): # circle's coordinates
        pass
    # if next_frame distance is negative: change speed and change coordinates in other way
    


#game Initialization
game = Game(WIDTH, HEIGHT, RADIUS)

# main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw
    win.fill((12, 24, 36))  
    game.draw(win)

    # update
    game.update()
    print(game.distance_to_circle())
    pygame.display.flip()

    clock.tick(120)