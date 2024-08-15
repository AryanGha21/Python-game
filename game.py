import pygame
import random
import math
#initialise pygame
pygame.init()

#screen
screen=pygame.display.set_mode((800,600))

background = pygame.image.load('background image.jpg')

# Title and Icon
pygame.display.set_caption("Space shooters")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#   player
playerImg = pygame.image.load('player.png')
playerX=370
playerY=480
playerX_change = 0

# enemy
enemyImg = []
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
no_of_enemy=6

for i in range(no_of_enemy):


    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

def reset_game():
    global playerX, playerY, playerX_change, bulletX, bulletY, bullet_state, score_val
    playerX = 370
    playerY = 480
    playerX_change = 0
    bulletX = 0
    bulletY = 480
    bullet_state = "ready"
    score_val = 0
    enemyImg.clear()
    enemyX.clear()
    enemyY.clear()
    enemyX_change.clear()
    enemyY_change.clear()
    for i in range(no_of_enemy):
        enemyImg.append(pygame.image.load('enemy.png'))
        enemyX.append(random.randint(0, 735))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(0.3)
        enemyY_change.append(40)

reset_game()


#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=0.9
bullet_state="ready"


# score
score_val = 0
font = pygame.font.Font('freesansbold.ttf',32)
Text_X=10
Text_Y=10

over_font=pygame.font.Font('freesansbold.ttf',64)


def show_score(x,y):
    score =font.render("Score :"+ str(score_val),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))


def player(x,y):
    screen.blit(playerImg,(x,y)) #to draw something

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollison(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2))+ (math.pow(enemyY - bulletY,2)))

    if distance<27:
        return True
    else:
        return False

#game loop game keeps running until quit button is not pressed
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running=False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change=-0.3
            if event.key == pygame.K_RIGHT:
                playerX_change=0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX=playerX # saves the cuurent x cordinate in bulletx so that it does not follow space ship
                    fire_bullet(bulletX,bulletY)
            if event.key == pygame.K_RETURN:
                reset_game()
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT  or event.key==pygame.K_SPACE:
                playerX_change=0
    
    
    playerX+=playerX_change
    if playerX <=0:
        playerX=0
    elif playerX>=736:
        playerX=736

    for i in range(no_of_enemy):

        #Game over
        if enemyY[i]>440:
             for j in range(no_of_enemy):
                 enemyY[j]=2000
             game_over()
             break

        enemyX[i]+=enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i]=0.3
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-0.3
            enemyY[i]+=enemyY_change[i]


        collison = isCollison(enemyX[i],enemyY[i],bulletX,bulletY)
        if collison:
            bulletY=480
            bullet_state="ready"
            score_val=score_val+1
            
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)


        enemy(enemyX[i],enemyY[i],i)

    
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change

   
    
    player(playerX,playerY)
    show_score(Text_X,Text_Y)
    
    pygame.display.update()
