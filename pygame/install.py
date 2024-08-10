# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    install.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/10 10:31:36 by pwolff            #+#    #+#              #
#    Updated: 2024/08/10 11:39:22 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
python3 -m venv env
source env/bin/activate
pip install pygame
pip list

pyhton3 -m pygame.examples.aliens


deactivate


https://pythonforge.com/pygame-creer-des-jeux-avec-python/


"""

import time


import pygame

pygame.init()
screen = pygame.display.set_mode((640, 455))
pygame.display.set_caption("** Créer un jeu avec PyGame **")

background = pygame.image.load("cielbleu.jpg").convert()

run = True
while run:
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:      
                run = False
        
        
        
        pygame.draw.circle(background, (250, 250, 0), (140, 60), 30)

        i = 0
        for i in range(100):
            
            screen.fill((0, 0, 0))
            screen.blit(background, (i, i))
            
            # pygame.draw.circle(background, (250, 250, 0), (140 + i, 60 + i), 30)
            time.sleep(0.005)

            pygame.display.update()
            # background = pygame.image.load("cielbleu.jpg").convert()
        # screen.fill((0, 0, 0))

pygame.quit()
quit()



background_image = "cielbleu.jpg"

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 455))

pygame.display.set_caption("Créer un jeu")
background = pygame.image.load(background_image).convert()


x, y = 0, 0
move_x, move_y = 0, 0
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -10
            elif event.key == K_RIGHT:
                move_x = +10
            elif event.key == K_UP:
                move_y = -10
            elif event.key == K_DOWN:
                move_y = +10
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            elif event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP:
                move_y = 0
            elif event.key == K_DOWN:
                move_y = 0
        x += move_x
        y += move_y
        screen.fill((0, 0, 0))
        screen.blit(background, (x, y))
        pygame.display.update()

pygame.quit()
quit()