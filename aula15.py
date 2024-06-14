# Instalar a biblioteca do panda
    # python -m pip install pygame
import pygame

pygame.init()

# Criar a tela do mp3
tela = pygame.display.set_mode((400,400),0,20)
# Título na barra
pygame.display.set_caption('Tocador de MP3')
branco = (255,255,255)

som = pygame.mixer.music.load('guns.mp3')
pygame.mixer.music.play()

play = True
pausar = True
run = True
volume = 1

# Estrutura de repetição para iniciar o play
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Criar os eventos
        if event.type == pygame.KEYDOWN:
            # Stop ou Play
            if event.key == pygame.K_s:
                if play == True:
                    play = False
                    pygame.mixer.music.stop()
                else:
                    play = True
                    pygame.mixer.music.play()
            # Pausar ou Reproduzir
            elif event.key == pygame.K_r:
                pygame.mixer.music.rewind()
            elif event.key == pygame.K_p:
                if pausar == False:
                    pausar = True
                    pygame.mixer.music.pause()
                else:
                    pausar = True
                    pygame.mixer.music.unpause()
            # Controle de Volume
            elif event.key == pygame.K_DOWN:
                # Valor flutuando de 0 a 1 decimal sendo 0 sem SOM e 1 volume maximo
                volume -= 0.1
                pygame.mixer.music.set_volume(volume)
            elif event.key == pygame.K_UP:
                # Valor flutuante de 0 a 1 decimal sendo 0 sem SOM e 1 Volume maximo
                volume -= 0.1
                pygame.mixer.music.set_volume(volume)
        tela.fill(branco)
        pygame.display.update()