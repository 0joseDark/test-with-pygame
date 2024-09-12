import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cenário 2D com Câmera")

# Definindo as cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Criando um grande cenário para simular uma "câmera"
WORLD_WIDTH = 2000
WORLD_HEIGHT = 2000
world = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))

# Preenchendo o cenário com um fundo simples e alguns objetos
world.fill(GREEN)
pygame.draw.rect(world, BLUE, (500, 500, 100, 100))  # Quadrado azul
pygame.draw.circle(world, RED, (1500, 1500), 50)     # Círculo vermelho

# Coordenadas da câmera
camera_x, camera_y = 0, 0

# Velocidade da câmera
camera_speed = 5

# Controle do mouse
mouse_control = False

# Função principal
def main():
    global camera_x, camera_y, mouse_control

    # Loop principal do jogo
    while True:
        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Habilitar controle do mouse quando o botão direito for pressionado
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:  # Botão direito do mouse
                    mouse_control = True
            
            # Desabilitar controle do mouse quando o botão direito for solto
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    mouse_control = False

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

        # Controle da câmera pelo mouse (se o botão direito estiver pressionado)
        if mouse_control:
            mouse_x, mouse_y = pygame.mouse.get_rel()
            camera_x -= mouse_x
            camera_y -= mouse_y

        # Limitar a câmera ao tamanho do mundo
        camera_x = max(min(camera_x, 0), SCREEN_WIDTH - WORLD_WIDTH)
        camera_y = max(min(camera_y, 0), SCREEN_HEIGHT - WORLD_HEIGHT)

        # Desenhar o mundo na posição correta da câmera
        screen.fill(WHITE)
        screen.blit(world, (camera_x, camera_y))

        # Atualizar a tela
        pygame.display.update()

# Rodar o jogo
if __name__ == "__main__":
    main()
