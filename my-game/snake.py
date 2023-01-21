import pygame
import time
import random 

# Inicializa o pygame
pygame.init()

# Cria a janela do jogo
width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo da cobrinha do Anderson")

# Define as cores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Variáveis do jogo
snake_block = 20
snake_speed = 90
tail = [] #lista
game_over_screen = pygame.display.set_mode((width, height))

# Carrega a coordenada da maça
appleX = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
appleY = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# Define as coordenadas iniciais da cobrinha
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0


# Carrega a fonte
font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width/2, height/2])

# Loop principal do jogo
run = True
while run:
    pygame.display.update()
    pygame.time.delay(snake_speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x1_change = -snake_block
        y1_change = 0
    elif keys[pygame.K_RIGHT]:
        x1_change = snake_block
        y1_change = 0
    elif keys[pygame.K_UP]:
        y1_change = -snake_block
        x1_change = 0
    elif keys[pygame.K_DOWN]:
        y1_change = snake_block
        x1_change = 0


    # Atualiza a posição da cobrinha
    x1 += x1_change
    y1 += y1_change

        # Verifica se a cobra saiu da tela
    if x1 >= width:
        x1 = 0
    if x1 < 0:
        x1 = width - snake_block
    if y1 >= height:
        y1 = 0
    if y1 < 0:
        y1 = height - snake_block
    win.fill(black)
   
    # Verifica se a cobra comeu a maçã
    if x1 <= appleX < x1 + snake_block and y1 <= appleY < y1 + snake_block:
        appleX = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        appleY = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        tail.append((x1, y1)) # adiciona as coordenadas atuais da cobra na lista 
       # snake_block += 10  # aumenta o tamanho da cobra
        

    

    # Desenha a cobra na tela
    pygame.draw.rect(win, white, [x1, y1, snake_block, snake_block])
    
    # Desenha a calda na tela
    for x, y in tail:
        pygame.draw.rect(win, white, [x, y, snake_block, snake_block])

    # Atualiza a posição da calda
    for i in range(len(tail)-1, 0, -1):
        tail[i] = tail[i-1]
    if len(tail) > 0:
        tail[0] = (x1, y1)

    # Verifica se a cobra alcançou a calda
    for x, y in tail[1:]:
         if x1 == x and y1 == y:
            run = False
        # Verifica se a cobra alcançou a calda
    for x, y in tail[1:]:
        if x1 == x and y1 == y:
            run = False
    for x, y in tail[1:]:
        if x1 == x and y1 == y:
            run = False
            message("Game Over", red, game_over_screen)
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.quit()
            

    # Desenha a maça na tela
    pygame.draw.rect(win, red, [appleX, appleY, snake_block, snake_block])

    # Desenha a maça na tela
    pygame.draw.rect(win, red, [appleX, appleY, snake_block, snake_block])

    #win.fill(black)
    pygame.draw.rect(win, white, [x1, y1, snake_block, snake_block])
    pygame.draw.rect(win, red, [appleX, appleY, snake_block, snake_block])

    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        run = False

