import pygame
import random
pygame.init()
SPRITE_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOUR_CHANGE_EVENT = pygame.USER.EVENT + 2
BLUE = pygame.Colour('blue')
LIGHTBLUE = pygame.Colour('lightblue')
DARKBLUE = pygame.Colour('darkblue')
YELLOW = pygame.Colour('yellow')
MAGENTA = pygame.Colour('magenta')
ORANGE = pygame.Colour('orange')
WHITE = pygame.Colour('white')
class Sprite(pygame.sprite.Sprite):
    def __init__ (self, colour, height, width):
        super(). __init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left<= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOUR_CHANGE_EVENT))
    def change_colour(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
def change_background_colour():
    global bg_colour
    bg_colour = random.choice([BLUE. LIGHTBLUE, DARKBLUE])
all_sprite_list = pygame.sprite.Group()
sp1 = Sprite(WHITE,20 , 30)
sp1.rect.x = random.randint(0, 400)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)
screen =pygame.display.set_caption("Boundary Sprite")
bg_colour =BLUE
screen.fill(bg_colour)
exit= False
colock = pygame.time.Clock()
while not exit:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame QUIT:
       exit = True
    elif event.type == BACKGROUND_COLOUR_CHANGE_EVENT:
      change_background_colour()
    all_sprite_list.update()
    screen.fill(bg_colour)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()

