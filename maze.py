from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Maze game")
background = transform.scale(image.load("background.jpg"), (700,500))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 595:
            self.direction = "left"
        
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color,wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
game = True
player = Player("hero.png", 0, 0, 5)
enemy = Enemy("cyborg.png", 470, 300, 2.7)
wall1 = Wall((155, 101, 61), 0, 450, 1000, 10)
chest = GameSprite("treasure.png", 600, 400, 10)
wall2 = Wall((155, 101, 61), 100, 0, 10, 300)
wall3 = Wall((155, 101, 61), 400, 100, 10, 360)

font.init()
font = font.SysFont("Arial", 70)
win = font.render(
    "You win!", True, (255, 215, 0))
lose = font.render(
    "You lose", True, (255, 0, 0))
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player.reset()
        enemy.reset()
        chest.reset()
        player.update()
        enemy.update()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        if sprite.collide_rect(player, chest):
            window.blit(win, (200,200))
            finish = True
            money.play()
        if sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, enemy):
            window.blit(lose, (200, 200))
            finish = True
            kick.play()
    display.update()


    
    