import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cenário 2D com Câmera e Menu")

# Definindo as cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

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

# Controle do mouse
mouse_control = False

# Variável para controlar o menu
menu_open = False
menu_position = (0, 0)

# Variável para controlar a seleção e movimento de quadrados
selected_square = None
moving_square = False

# Tamanho padrão do quadrado azul
SQUARE_SIZE = 50

# Função para desenhar o menu
def draw_menu(position):
    menu_width = 120
    menu_height = 100
    pygame.draw.rect(screen, BLACK, (*position, menu_width, menu_height))
    
    # Desenhando as opções do menu
    font = pygame.font.SysFont(None, 24)
    create_text = font.render("Criar", True, WHITE)
    delete_text = font.render("Apagar", True, WHITE)
    move_text = font.render("Mover", True, WHITE)
    
    screen.blit(create_text, (position[0] + 10, position[1] + 10))
    screen.blit(delete_text, (position[0] + 10, position[1] + 40))
    screen.blit(move_text, (position[0] + 10, position[1] + 70))

# Função principal
def main():
    global camera_x, camera_y, mouse_control, menu_open, menu_position, selected_square, moving_square

    # Loop principal do jogo
    while True:
        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Clique do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo
                    if menu_open:
                        # Verificar se o clique foi em uma das opções do menu
                        mx, my = pygame.mouse.get_pos()
                        if menu_position[0] <= mx <= menu_position[0] + 120:
                            if menu_position[1] <= my <= menu_position[1] + 30:
                                # Criar quadrado
                                mouse_x, mouse_y = pygame.mouse.get_pos()
                                # Corrigir posição em relação à câmera
                                real_x = mouse_x - camera_x
                                real_y = mouse_y - camera_y
                                blue_squares.append(pygame.Rect(real_x, real_y, SQUARE_SIZE, SQUARE_SIZE))
                            elif menu_position[1] + 30 <= my <= menu_position[1] + 60 and selected_square:
                                # Apagar quadrado
                                blue_squares.remove(selected_square)
                                selected_square = None
                            elif menu_position[1] + 60 <= my <= menu_position[1] + 90 and selected_square:
                                # Mover quadrado
                                moving_square = True
                            menu_open = False
                    else:
                        # Verificar se o clique foi em um quadrado existente
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        real_x = mouse_x - camera_x
                        real_y = mouse_y - camera_y
                        selected_square = None
                        for square in blue_squares:
                            if square.collidepoint(real_x, real_y):
                                selected_square = square
                                break
                elif event.button == 3:  # Botão direito do mouse
                    # Abrir menu no ponto clicado
                    menu_open = True
                    menu_position = pygame.mouse.get_pos()
            
            # Soltar o botão do mouse
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    moving_square = False
            
            # Movimentar quadrado com o mouse
            if event.type == pygame.MOUSEMOTION and moving_square and selected_square:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                real_x = mouse_x - camera_x
                real_y = mouse_y - camera_y
                selected_square.x = real_x - SQUARE_SIZE // 2
                selected_square.y = real_y - SQUARE_SIZE // 2

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

        # Desenhar os quadrados azuis
        for square in blue_squares:
            pygame.draw.rect(world, BLUE, square)

        # Desenhar o menu, se aberto
        if menu_open:
            draw_menu(menu_position)

        # Atualizar a tela
        pygame.display.update()

# Rodar o jogo
if __name__ == "__main__":
    main()
