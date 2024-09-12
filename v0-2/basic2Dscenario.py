import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cenário 2D com Câmera e Criação de Quadrados")

# Definindo as cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Criando um grande cenário para simular uma "câmera"
WORLD_WIDTH = 2000
WORLD_HEIGHT = 2000
world = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))

# Preenchendo o cenário com um fundo simples
world.fill(GREEN)

# Lista de quadrados azuis no cenário
blue_squares = []

# Coordenadas da câmera
camera_x, camera_y = 0, 0

# Velocidade da câmera
camera_speed = 5

# Tamanho padrão do quadrado azul
SQUARE_SIZE = 50

# Função principal
def main():
    global camera_x, camera_y

    # Loop principal do jogo
    while True:
        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Clique do mouse para criar quadrados azuis
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Corrigir posição em relação à câmera
                    real_x = mouse_x - camera_x
                    real_y = mouse_y - camera_y
                    blue_squares.append(pygame.Rect(real_x, real_y, SQUARE_SIZE, SQUARE_SIZE))

        # Pegar as teclas pressionadas
        keys = pygame.key.get_pressed()

        # Movimentação da câmera com as teclas de seta
        if keys[pygame.K_LEFT]:
            camera_x += camera_speed
        if keys[pygame.K_RIGHT]:
            camera_x -= camera_speed
        if keys[pygame.K_UP]:
            camera_y += camera_speed
        if keys[pygame.K_DOWN]:
            camera_y -= camera_speed

        # Limitar a câmera ao tamanho do mundo
        camera_x = max(min(camera_x, 0), SCREEN_WIDTH - WORLD_WIDTH)
        camera_y = max(min(camera_y, 0), SCREEN_HEIGHT - WORLD_HEIGHT)

        # Desenhar o mundo na posição correta da câmera
        screen.fill(WHITE)
        screen.blit(world, (camera_x, camera_y))

        # Desenhar os quadrados azuis
        for square in blue_squares:
            pygame.draw.rect(world, BLUE, square)

        # Atualizar a tela
        pygame.display.update()

# Rodar o jogo
if __name__ == "__main__":
    main()
