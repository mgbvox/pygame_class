import pygame
import sys
import numpy as np
from pygame_custom_tools import *
import string
from pygame.locals import *


#words = get_words()


if __name__ == '__main__':

    #Pane implements a basic interactive window.

    hw = (1080,1920)
    window_color = (93, 221, 174)
    pane = Pane(area=hw, fill=window_color)

    rect_color = np.random.uniform(0, 255, 3).astype(int)
    dims = np.random.uniform(0, 400, 4).astype(int)
    pane.addRect(color=rect_color, dims=dims)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()





        rect_color = np.random.uniform(0,255,3).astype(int)
        txt_color = np.random.uniform(0, 255, 3).astype(int)
        dims = np.random.uniform(0,1920,4).astype(int)
        #txt = np.random.choice(words,1)[0]

        pos = np.random.uniform(0,1920,2).astype(int)

        pane.addRect(color=rect_color, dims=dims)
        pane.addText(txt="DON'T TOUCH!", color=txt_color, pos=pos,
                     font_size=np.random.randint(10,500))