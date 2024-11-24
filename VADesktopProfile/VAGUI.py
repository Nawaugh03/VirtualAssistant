import time
import random
#import os
import math
#import random
import pygame
import threading
import sys

class Frame:
    def __init__(self,screen):
        self.screen=screen
        self._online=False
        self._buttonwidth=100
        self._buttonheight=50
        self._buttons=[]
        self._buttontext=[]
        self.__desired_width=1200
        self.__desired_height=720
    def _draw(self):
        pass
    def _readbuttoninput(self):
        pass
    def animate(self):
        pass
class GUI():
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.setmode((1200,720), pygame.RESIZABLE)
        pygame.display.set_caption('Task Assistant RPG')
        self.currentframe=""
        self.running=True
        self.run()
    def run(self):
        while self.running:
            pass
        pygame.quit()
        sys.exit()

if __name__ in "__main__":
    GUI()