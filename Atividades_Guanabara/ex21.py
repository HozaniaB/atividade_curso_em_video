 # 21 - Faça um programa em Puthon que abra e reproduza o áudio de um arquivo em MP3.  
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("ex21.mp3")
pygame.mixer.music.play()
pygame.event.wait()
