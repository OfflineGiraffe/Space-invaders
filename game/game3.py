import pygame
import random
import os
pygame.init()

pygame.display.set_caption("First project")
win = pygame.display.set_mode((500, 500))


bg = pygame.image.load(os.path.join("data", "bruh1.png"))
bg2 = pygame.image.load(os.path.join("data", "bruh2.png"))
char = pygame.image.load(os.path.join("data", "bruh4.png")), pygame.image.load(os.path.join("data", "bruh10.png"))
title = pygame.image.load(os.path.join("data", "bruh8.png"))
powerup = pygame.image.load(os.path.join("data", "bruh5.png"))
banana = pygame.image.load(os.path.join("data", "bruh7.png"))
bananax = 30
bananay = 300
titlex = 0
bgX = 0
bg2X = bg.get_width()
scorex = 390
walkcount = 0

class person(object):
    def __init__(self, x, y, radius, width):
        self.x = x
        self.y = y
        self.radius = radius
        self.width = width
        self.vel = 10
        self.hitbox = (self.x + 30, self.y, 20, 20)

    def draw(self, win):
        global walkcount
        if walkcount + 1 >= 6:
            walkcount = 0
        win.blit(char[walkcount//3], (circle.x, circle.y))
        walkcount += 1
        self.hitbox = (self.x, self.y, 20, 20)


    def hit(self):
        i = 0
        font1 = pygame.font.SysFont("comicsans", 50)
        text = font1.render("You Lose! Score:  " + str(score), 1, (0, 0, 0))
        win.blit(text, (100, 200))
        pygame.display.update()
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


class enemy(object):
    def __init__(self, x, y, radius, width):
        self.x = x
        self.y = y
        self.radius = radius
        self.width = width
        self.vel = 10
        self.hitbox1 = (self.x, self.y, 20, 20)

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 255), (self.x, self.y), self.radius, self.width)
        self.hitbox1 = (self.x - 20, self.y + 20, 40, -40)

    def hit1(self):
        circle2.y = random.randint(0, 500)
        circle2.x = 700

    def hit(self):
        circle3.y = random.randint(0, 500)
        circle3.x = 1000


class projectile(object):
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.vel = 5

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)


class powerupobject(object):
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.vel = 5
        self.hitbox = (self.x, self.y, 30, 30)

    def draw(self, win):
        win.blit(powerup, (powerupitem.x, powerupitem.y))
        self.hitbox = (self.x, self.y, 30, 30)

    def hit(self):
        powerupitem.y = random.randint(0, 500)
        powerupitem.x = 1500
        circle2.vel -= 7
        circle3.vel -= 7


def redrawWindow1():
    global scorex
    win.blit(bg, (int(bgX), 0))
    win.blit(bg2, (int(bg2X), 0))
    circle.draw(win)
    circle2.draw(win)
    circle3.draw(win)
    powerupitem.draw(win)
    text = font.render("Score: " + str(score), 1, (0, 0, 0))
    if score >= 100:
        scorex = 370
    win.blit(text, (scorex, 10))
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


def scroll():
    if circle2.x < -20:
        circle2.x = 700
        circle2.y = random.randint(0, 500)
    if circle3.x < -20:
        circle3.x = 1100
        circle3.y = random.randint(0, 500)
    if powerupitem.x < -30:
        powerupitem.x = 1500
        powerupitem.y = random.randint(0, 500)


def redrawWindow2():
    win.blit(title, (titlex, 0))
    pygame.display.update()


powerupitem = powerupobject(1500, 300, 30, 30)
circle = person(20, 400, 20, 10)
circle2 = enemy(800, 400, 20, 0)
circle3 = enemy(1000, 200, 20, 0)
font = pygame.font.SysFont("comicsans", 30, True)
fps = 20
count = 0
shootloop = 0
bullets = []
score = 0
timer = 0
run = True
while run:
    redrawWindow2()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.y + bullet.radius > circle2.hitbox1[1] + circle2.hitbox1[3] and bullet.y - bullet.radius < circle2.hitbox1[1]:
            if bullet.x + bullet.radius > circle2.hitbox1[0]:
                circle2.hit1()
                score += 1
                bullets.pop(bullets.index(bullet))
        if bullet.y + bullet.radius > circle3.hitbox1[1] + circle3.hitbox1[3] and bullet.y - bullet.radius < circle3.hitbox1[1]:
            if bullet.x + bullet.radius > circle3.hitbox1[0]:
                circle3.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
        if 0 < bullet.x < 700:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if shootloop > 0:
        shootloop += 1
    if shootloop > 20:
        shootloop = 0

    if circle.hitbox[1] + circle.hitbox[3] > circle2.hitbox1[1] + circle2.hitbox1[3] and circle.hitbox[1] < circle2.hitbox1[1]:
        if circle.hitbox[0] + circle.hitbox[2] > circle2.hitbox1[0] and circle.hitbox[0] < circle2.hitbox1[0] + circle2.hitbox1[2]:
            circle.hit()
    if circle.hitbox[1] + circle.hitbox[3] > circle3.hitbox1[1] + circle3.hitbox1[3] and circle.hitbox[1] < circle3.hitbox1[1]:
        if circle.hitbox[0] + circle.hitbox[2] > circle3.hitbox1[0] and circle.hitbox[0] < circle3.hitbox1[0] + circle3.hitbox1[2]:
            circle.hit()
    if circle.hitbox[1] + circle.hitbox[3] > powerupitem.hitbox[1] and circle.hitbox[1] < powerupitem.hitbox[1] + powerupitem.hitbox[3]:
        if circle.hitbox[0] + circle.hitbox[2] > powerupitem.hitbox[0] and circle.hitbox[0] < powerupitem.hitbox[0] + powerupitem.hitbox[2]:
            powerupitem.hit()
            timer = 0
    if circle2.hitbox1[1] + circle2.hitbox1[3] > circle3.hitbox1[1] and circle2.hitbox1[1] < circle3.hitbox1[1] + circle3.hitbox1[3]:
        if circle2.hitbox1[0] + circle2.hitbox1[2] > circle3.hitbox1[0] and circle2.hitbox1[0] < circle3.hitbox1[0] + circle3.hitbox1[2]:
            circle3.x = 1000
    if timer != 100:
        timer += 1
    if timer == 100:
        circle2.vel = 10
        circle3.vel = 10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_ENTER]:
        count += 1
    if count > 1:
        redrawWindow1()
        titlex = 500
        circle3.x -= circle3.vel
        circle2.x -= circle2.vel
        powerupitem.x -= powerupitem.vel
    if keys[pygame.K_DOWN]:
        if circle.y < 490:
            circle.y += circle.vel
    if keys[pygame.K_UP]:
        if circle.y > 10:
            circle.y -= circle.vel
    if keys[pygame.K_LEFT]:
        if circle.x > 0:
            circle.x -= circle.vel
    if keys[pygame.K_RIGHT]:
        if circle.x < 490:
            circle.x += circle.vel
    if keys[pygame.K_SPACE] and shootloop == 0:
        if len(bullets) < 10:
            bullets.append(projectile(circle.x + circle.radius, round(circle.y + circle.width), 6, (255, 255, 255)))
        shootloop = 1
        walkcount = 0

    pygame.time.delay(fps)
    bgX -= 1.4
    bg2X -= 1.4
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bg2X < bg2.get_width() * -1:
        bg2X = bg2.get_width()
    scroll()

pygame.quit()