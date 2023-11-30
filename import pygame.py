import pygame

# Constantes e Configurações
WIDTH, HEIGHT = 500, 500
VEL = 5
JUMP_HEIGHT = 10
OBSTACLE_VEL = 1
FPS = 30

# Inicialização do Pygame
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Carrega as imagens
background = pygame.image.load("intro.png")  # Substituí "background.jpg" por "intro.jpg"
boneco = pygame.image.load('idle.png')
collectible = pygame.image.load('coin.png')
obstacle = pygame.image.load('brick.png')

# Posições iniciais
x, y = 50, 425
collectibleX, collectibleY = 200, 200
obstacleX, obstacleY = 500, 450

# Variáveis de jogo
jumping = False
jumpHeight = JUMP_HEIGHT
score = 0
totalJumps = 0

# Fonte
font = pygame.font.Font(None, 36)

def draw_score():
    text = font.render(f'Pulos: {totalJumps}', True, (255, 255, 255))
    win.blit(text, (350, 10))

def game_over():
    text = font.render('GAME OVER', True, (250, 250, 250))
    win.blit(text, (200, 250))
    pygame.display.update()
    pygame.time.wait(2000)

# Loop principal
run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= VEL
    if keys[pygame.K_RIGHT]:
        x += VEL

    if not jumping:
        if keys[pygame.K_UP]:
            jumping = True
            totalJumps += 1
    else:
        if jumpHeight >= -JUMP_HEIGHT:
            neg = 1
            if jumpHeight < 0:
                neg = -1
            y -= (jumpHeight ** 2) * 0.5 * neg
            jumpHeight -= 1
        else:
            jumping = False
            jumpHeight = JUMP_HEIGHT

    obstacleX -= OBSTACLE_VEL
    if obstacleX < -64:
        obstacleX = WIDTH

    if x < collectibleX < x + 64 and y < collectibleY < y + 64:
        score += 1

    if x < obstacleX < x + 64 and y < obstacleY < y + 64:
        game_over()
        run = False

    win.blit(background, (0, 0))  # Desenha o fundo primeiro
    win.blit(collectible, (collectibleX, collectibleY))
    win.blit(obstacle, (obstacleX, obstacleY))
    win.blit(boneco, (x, y))

    draw_score()

    pygame.display.update()

pygame.quit()

print(f'Você coletou {score} objetos!')
print(f'Você pulou {totalJumps} vezes!')
