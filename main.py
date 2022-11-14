import pygame
from pygame import mixer
import sys
import random
import math

# inicializa o pygame
pygame.init()

# cria a tela
def tela(x, y):
    global screen
    screen = pygame.display.set_mode((x, y))
x_pix = 800
y_pix = 600
tela(x_pix, y_pix)

# Title and icon
pygame.display.set_caption("Space Invaders")
# adicionar icon dps
    
# plano de fundo
background = pygame.image.load('./img/MENU.png')

# background sound
background_sound = pygame.mixer.Sound('./sounds/background.wav')
# para o som tocar em loop:
background_sound.play(-1)

# Player
playerImg = pygame.image.load('./img/001-nave-espacial.png')
def def_player(x,y):
    global playerX, playerY, playerX_change
    playerX = x/2 - 30
    playerY = y - 120
    playerX_change = 0
def_player(x_pix, y_pix)

# Enemy
num_for_enemies = 6
enemySkin = pygame.image.load('./img/002-ghost.png')
enemySkin2 = pygame.image.load('./img/003-ghost.png')
def def_enemy(x):

    global enemyImg,enemyX,enemyY,enemyX_change,enemyY_change,enemy_state
    enemyImg = enemySkin
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    enemy_state = []

    # tiro do inimigo
    global enemy_bulletX,enemy_bulletY,enemy_bulletY_change,v
    v = 0.5
    enemy_bulletX = []
    enemy_bulletY = []
    enemy_bulletY_change = []

    for i in range(num_for_enemies):
        enemyX.append(random.randint(65, x - 65))
        enemyY.append(random.randint(75, 150))
        enemyX_change.append(v)
        enemyY_change.append(40)
        enemy_state.append("ready")
        enemy_bulletX.append(enemyX[i])
        enemy_bulletY.append(enemyY[i])
        enemy_bulletY_change.append(enemyY_change[i])
def_enemy(x_pix)

# Bullet: parada --> não consegue ver na tela
# Bullet: fire --> atirando (movendo)
bulletImg = pygame.image.load('./img/001-bullet.png')
def bullet(y):
    global bulletX, bulletY, bulletX_change, bulletY_change, bullet_state
    bulletX = 0
    bulletY = y - 120
    bulletX_change = 0
    bulletY_change = 3
    bullet_state = 'parada'
bullet(y_pix)

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


enemy_bulletImg = pygame.image.load('./img/enemy_bullet.png')
def enemy_bullet(x, y, i):
    screen.blit(enemy_bulletImg, (x[i], y[i]))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    if distance < 30:
        return True
    else:
        return False


def coliep(x, y, z, k):
    d = math.sqrt((x - z) ** 2 + (y - k) ** 2)
    if d < 27:
        return True
    else:
        return False


def restart():
    global MENU, GAME, score
    tela(x_pix, y_pix)
    def_player(x_pix, y_pix)
    def_enemy(x_pix)
    bullet(y_pix)
    MENU = True
    GAME = False
    score = 0

# mudar resolucao
def change_res(x, y):
    global num_for_enemies, x_pix, y_pix
    x_pix = x
    y_pix = y
    tela(x, y)
    def_player(x, y)
    num_for_enemies = int(x * y / 80000)
    def_enemy(x)
    bullet(y)

# definir telas
MENU = True
menu = pygame.image.load('./img/MENU.png')
OPT = False
opt = pygame.image.load('./img/opt.jpg')
RES = False
res = pygame.image.load('./img/res.jpg')
CSS = False
css = pygame.image.load('./img/css.jpg')
NAVE = False
nave = pygame.image.load('./img/nave.jpg')
MONSTER = False
monster = pygame.image.load('./img/monster.jpg')
BALA = False
bala = pygame.image.load('./img/bala.jpg')
GAME = False
game = pygame.image.load('./img/space-trip-colorful-digital-art.jpg')
gameover = pygame.image.load('./img/game.over-ic.png')

while True:
    # RGB
    screen.fill((0, 0, 0))
    # Plano de fundo
    screen.blit(background, (0, 0))

    if MENU:
        background = menu
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        background = game
                        GAME = True
                        MENU = False
                if event.key == pygame.K_ESCAPE:
                    OPT = True
                    MENU = False

    if OPT:
        background = opt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    MENU = True
                    OPT = False
                if event.key == pygame.K_s:
                    RES = True
                    OPT = False
                if event.key == pygame.K_c:
                    CSS = True
                    OPT = False

    if RES:
        background = res
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    OPT = True
                    RES = False
                if event.key == pygame.K_1:
                    menu = pygame.image.load('./img/MENU1.png')
                    opt = pygame.image.load('./img/opt1.jpg')
                    res = pygame.image.load('./img/res1.jpg')
                    css = pygame.image.load('./img/css1.jpg')
                    nave = pygame.image.load('./img/nave1.jpg')
                    monster = pygame.image.load('./img/monster1.jpg')
                    bala = pygame.image.load('./img/bala1.jpg')
                    game = pygame.image.load('./img/game1.jpg')
                    gameover = pygame.image.load('./img/game.over1-ic.png')
                    change_res(1024, 768)
                if event.key == pygame.K_ESCAPE:
                    menu = pygame.image.load('./img/MENU.png')
                    opt = pygame.image.load('./img/opt.jpg')
                    res = pygame.image.load('./img/res.jpg')
                    css = pygame.image.load('./img/css.jpg')
                    nave = pygame.image.load('./img/nave.jpg')
                    monster = pygame.image.load('./img/monster.jpg')
                    bala = pygame.image.load('./img/bala.jpg')
                    game = pygame.image.load('./img/game.jpg')
                    gameover = pygame.image.load('./img/game.over-ic.png')
                    change_res(800, 600)

    if CSS:
        background = css
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    OPT = True
                    CSS = False
                if event.key == pygame.K_1:
                    NAVE = True
                    CSS = False
                if event.key == pygame.K_2:
                    MONSTER = True
                    CSS = False
                if event.key == pygame.K_3:
                    BALA = True
                    CSS = False

                if event.key == pygame.K_ESCAPE:
                    playerImg = pygame.image.load('./img/001-nave-espacial.png')
                    enemySkin = pygame.image.load('./img/002-ghost.png')
                    bulletImg = pygame.image.load('./img/001-bullet.png')
                    enemySkin = pygame.image.load('./img/002-ghost.png')
                    enemySkin2 = pygame.image.load('./img/003-ghost.png')
                    def_enemy(x_pix)

    if NAVE:
        background = nave
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    CSS = True
                    NAVE = False
                if event.key == pygame.K_1:
                    playerImg = pygame.image.load('./img/aircraft.png')
                    CSS = True
                    NAVE = False
                if event.key == pygame.K_2:
                    playerImg = pygame.image.load('./img/rocket.png')
                    CSS = True
                    NAVE = False
                if event.key == pygame.K_3:
                    playerImg = pygame.image.load('./img/ufo.png')
                    CSS = True
                    NAVE = False
                if event.key == pygame.K_4:
                    playerImg = pygame.image.load('./img/tardis.png')
                    CSS = True
                    NAVE = False
                if event.key == pygame.K_5:
                    playerImg = pygame.image.load('./img/K9.png')
                    CSS = True
                    NAVE = False
                if event.key == pygame.K_ESCAPE:
                    playerImg = pygame.image.load('./img/001-nave-espacial.png')
                    CSS = True
                    NAVE = False
    
    if MONSTER:
        background = monster
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    CSS = True
                    MONSTER = False
                if event.key == pygame.K_1:
                    enemySkin = pygame.image.load('./img/000-ghost.png')
                    enemySkin2 = pygame.image.load('./img/001-ghost.png')
                    CSS = True
                    MONSTER = False
                if event.key == pygame.K_2:
                    enemySkin = pygame.image.load('./img/004-ghost.png')
                    enemySkin2 = pygame.image.load('./img/005-ghost.png')
                    CSS = True
                    MONSTER = False
                if event.key == pygame.K_3:
                    enemySkin = pygame.image.load('./img/ufo-1.png')
                    enemySkin2 = pygame.image.load('./img/ufo-2.png')
                    CSS = True
                    MONSTER = False
                if event.key == pygame.K_4:
                    enemySkin = pygame.image.load('./img/dalek.png')
                    enemySkin2 = pygame.image.load('./img/dalek-2.png')
                    CSS = True
                    MONSTER = False
                if event.key == pygame.K_5:
                    enemySkin = pygame.image.load('./img/cyberman.png')
                    enemySkin2 = pygame.image.load('./img/cyberman-2.png')
                    CSS = True
                    MONSTER = False
                if event.key == pygame.K_ESCAPE:
                    enemySkin = pygame.image.load('./img/002-ghost.png')
                    enemySkin2 = pygame.image.load('./img/003-ghost.png')
                    CSS = True
                    MONSTER = False
            def_enemy(x_pix)

    if BALA:
        background = bala
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    CSS = True
                    BALA = False
                if event.key == pygame.K_1:
                    bulletImg = pygame.image.load('./img/003-bullet.png')
                    CSS = True
                    BALA = False
                if event.key == pygame.K_2:
                    bulletImg = pygame.image.load('./img/002-bullet.png')
                    CSS = True
                    BALA = False
                if event.key == pygame.K_3:
                    bulletImg = pygame.image.load('./img/004-bullet.png')
                    CSS = True
                    BALA = False
                if event.key == pygame.K_4:
                    bulletImg = pygame.image.load('./img/laser.png')
                    CSS = True
                    BALA = False
                if event.key == pygame.K_5:
                    bulletImg = pygame.image.load('./img/laser2.png')
                    CSS = True
                    BALA = False
                if event.key == pygame.K_ESCAPE:
                    bulletImg = pygame.image.load('./img/001-bullet.png')
                    CSS = True
                    BALA = False

    if GAME:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -1*(x_pix*y_pix)/(800*600)
                if event.key == pygame.K_RIGHT:
                    playerX_change = (x_pix*y_pix)/(800*600)

                if event.key == pygame.K_SPACE:
                    if background != gameover:
                        if bullet_state == 'parada':
                            bullet_sound = mixer.Sound('./sounds/laser.wav')
                            bullet_sound.play()
                            bulletX = playerX
                            fire_bullet(bulletX, bulletY)
                if event.key == pygame.K_r:
                    restart()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and playerX_change != (x_pix*y_pix)/(800*600):
                    playerX_change = 0
                if event.key == pygame.K_RIGHT and playerX_change != -1*(x_pix*y_pix)/(800*600):
                    playerX_change = 0

        playerX += playerX_change

        # garante q não saia da tela:
        if playerX <= 0:
            playerX = 0

        elif playerX >= x_pix - 64:
            playerX = x_pix - 64

        for i in range(num_for_enemies):

            if enemyX[i] <= 0:
                enemyX_change[i] = v*(x_pix*y_pix)/(800*600)
                enemyY[i] += enemyY_change[i]

            elif enemyX[i] >= x_pix - 64:
                enemyX_change[i] = -1*v*(x_pix*y_pix)/(800*600)
                enemyY[i] += enemyY_change[i]
            
            enemyX[i] += enemyX_change[i]
            # colisão
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)

            #bala do inimigo
            if i%3 == 0:
                if enemy_bulletY[i] >= y_pix:
                    enemy_bulletY[i] = enemyY[i]
                    enemy_bulletX[i] = enemyX[i]
                if enemy_bulletY[i] <= y_pix:
                    enemy_bulletY_change[i] = (x_pix*y_pix)/(800*600)*v/2
                    enemy_bulletY[i] += enemy_bulletY_change[i]
                enemy_bullet(enemy_bulletX, enemy_bulletY, i)

            
            if collision:
                collision_sound = mixer.Sound('./sounds/explosion.wav')
                collision_sound.play()
                bulletY = y_pix - 120
                bullet_state = 'parada'
                score += 1
                enemyX[i] = random.randint(65, x_pix - 65)
                enemyY[i] = random.randint(50, 150)
            
           

            ep = coliep(enemyX[i], enemyY[i], playerX, playerY)
            bp = coliep(enemy_bulletX[i], enemy_bulletY[i], playerX, playerY)

            if ep or bp:
                playerX = x_pix
                playerY = y_pix
                for c in range(num_for_enemies):
                    enemyX[c] = enemy_bulletX[c] = x_pix
                    enemyY[c] = enemy_bulletY[c] = y_pix
                background = gameover
                gameover_sound = pygame.mixer.Sound('./sounds/gameover.wav')
                gameover_sound.play()
                background_sound.stop()
             
            enemy(enemyX[i], enemyY[i])

        # movimento da bala
        if bulletY <= 0:
            bulletY = y_pix - 120
            bullet_state = 'parada'

        if bullet_state == 'fire':
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        # texto score
        font = pygame.font.SysFont('calibri', 24)
        text = font.render(f'SCORE: {score}', True, 'blue', 'black')
        textRect = text.get_rect()
        textRect.center = (45, 12)
        screen.blit(text, textRect)

        # dificuldades
        if score == 10:
            enemyImg = enemySkin2
            v = 1
        
    pygame.display.update()
