import pygame
import requests
import sys
import numpy as np

white = (255,255,255)
black = (0,0,0)

'''
def get_words():
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    return [i.decode("utf-8") for i in response.content.splitlines()]
'''



class Pane(object):
    def __init__(self, area=(600, 400), fill=(white)):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen.fill(fill)
        pygame.display.update()

    def addRect(self, color=(black), dims=(175, 75, 200, 100)):
        self.rect = pygame.draw.rect(self.screen, color, dims)
        pygame.display.update()

    def addText(self,txt,color,pos,font_size=25):
        self.font = pygame.font.SysFont('Arial', font_size)
        self.screen.blit(self.font.render(txt, True, color), pos)
        pygame.display.update()