import pygame
import os
import time
import random

pygame.font.init()
from Feed_Forward_Neural_Network import *

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Tutorial")

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))

GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player player
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
YELLOW_SPACE_SHIP = pygame.transform.scale(YELLOW_SPACE_SHIP, (50, 45))
# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
RED_LASER = pygame.transform.scale(RED_LASER, (50, 45))

GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
GREEN_LASER = pygame.transform.scale(GREEN_LASER, (50, 45))

BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
BLUE_LASER = pygame.transform.scale(BLUE_LASER, (50, 45))

YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
YELLOW_LASER = pygame.transform.scale(YELLOW_LASER, (50, 45))
# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)


class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        global score
        global reward
        self.cooldown()
        flag = False
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                # reward -= (100-obj.health)
                reward -= 5
                obj.health -= 10
                self.lasers.remove(laser)
                flag = True
        return flag

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        flag = False
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        flag = True
                        if laser in self.lasers:
                            self.lasers.remove(laser)
        return flag

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
        self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health / self.max_health),
        10))


class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x + 5, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def get_inputs(enemies, player):

    # Config 1
    # inputs = []
    # x = -1
    # maxy = -1
    # bullets = []
    # for i in range(0, 20):
    #     inputs.append(0)
    #
    #
    # lasers = []
    # for laser in player.lasers:
    #     lasers.append(laser.x)
    # for enemy in enemies:
    #     flag = False
    #     for l in range(enemy.x - 10, enemy.x + 10):
    #         if l in lasers:
    #             flag = True
    #     if not flag:
    #         if maxy < enemy.y:
    #             maxy = enemy.y
    #             x = enemy.x
    #
    #     for laser in enemy.lasers:
    #         inputs[laser.x // 51] = max(inputs[laser.x // 51],laser.x - player.x)
    #         inputs[laser.y // 51 + 10] = max(inputs[laser.y//51 + 10],laser.y - player.y)
    #
    # inputs.append(x - player.x)
    # # print(inputs)
    # return np.array(inputs)


    # configuration 2

    inputs = []
    x = -1
    maxy = -1
    bullets = []
    for i in range(0, 10):
        inputs.append(0)

    # Config 1
    lasers = []
    for laser in player.lasers:
        lasers.append(laser.x)
    for enemy in enemies:
        flag = False
        for l in range(enemy.x - 10, enemy.x + 10):
            if l in lasers:
                flag = True
                break
        if not flag:
            if maxy < enemy.y:
                maxy = enemy.y
                x = enemy.x

    inputs.append(x - player.x)
    # print(inputs)
    return np.array(inputs)

score = 0
reward = 0


def main(weights):
    global score
    global reward
    score = 0
    reward = 0
    run = True
    FPS = 60
    level = 0
    lives = 1
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 5
    enemy_vel = 1
    W1, W2 = get_weights_from_encoded(weights)
    player_vel = 5
    laser_vel = 5

    player = Player(300, 430)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WIN.blit(BG, (0,0))
        # draw text
        lives_label = main_font.render(f"Score: {score}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            return score, reward
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            if level <= 5:
                wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),
                              random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_a] and player.x - player_vel > 0: # left
        #     player.x -= player_vel
        # if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
        #     player.x += player_vel
        # if keys[pygame.K_w] and player.y - player_vel > 0: # up
        #     player.y -= player_vel
        # if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
        #     player.y += player_vel
        # if keys[pygame.K_SPACE]:
        #     player.shoot()

        output = np.argmax(np.array(forward_propagation(get_inputs(enemies, player), W1, W2)))
        if output == 0 and player.x - player_vel > 0:
            player.x -= player_vel
        elif output == 1 and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel
        else:
            player.shoot()

        # print(get_inputs(enemies,player))
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, (level) * 60) == 1:
                enemy.shoot()

            if level > 2:
                if random.randrange(0, 3 * 60) == 1:
                    if random.randrange(0, 2) == 1 and enemy.x < 420:
                        enemy.x += 30
                    else:
                        if enemy.x >= 30:
                            enemy.x -= 30

            if collide(enemy, player):
                player.health -= 100
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        if player.move_lasers(-laser_vel, enemies):
            score += 10
            reward += 10

    return score, reward


def main_menu(weights):
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        pygame.display.update()

        return main(weights)

    pygame.quit()

# main_menu()
