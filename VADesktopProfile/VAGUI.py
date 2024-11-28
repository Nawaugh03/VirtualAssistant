import time
import random
#import os
import math
import random
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
        self._desired_width=1200
        self._desired_height=720
    def _draw(self):
        pass
    def _readbuttoninput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._online=False
            if event.type == pygame.VIDEORESIZE:
                width, height=event.w, event.h
                self.screen=pygame.display.set_mode((width, height),pygame.RESIZABLE)
    def _animate(self):
        pass
class OpeningFrame(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.Radius=10
        self.screen.fill(self.BLACK)
        self.StarBackground = True
        # Star properties
        self.NUM_STARS = 200
        self.stars = [self. generate_star()
                      for _ in range(self.NUM_STARS)
                      ]
        
    def generate_star(self):
        """Generate a star on a circle around the center."""
        CENTER_X = self._desired_width // 2 
        CENTER_Y = self._desired_height // 2
        angle = random.uniform(0, 2 * math.pi)  # Random angle in radians
        x = CENTER_X + self.Radius * math.cos(angle)
        y = CENTER_Y + self.Radius * math.sin(angle)
        size = random.randint(1, 2)
        
        # Calculate outward velocity (dx, dy)
        dx = math.cos(angle) * random.uniform(1, 2) *1.5
        dy = math.sin(angle) * random.uniform(1, 2) *1.5
        return [x, y, size, dx, dy]
 
    def _animate(self):
            
        #while (self.StarBackground):
            self.screen.fill(self.BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.online = False
                        
                # Update and draw stars
            for i,star in enumerate(self.stars):
                x, y, size, dx, dy = star

                # Move the star
                x += dx
                y += dy

                # Increase size to simulate getting closer
                size += 0.02
    

                # Check if the star is out of bounds
                if x < 0 or y < 0 or x > self._desired_width or y > self._desired_height:
                    self.stars[i]= self.generate_star()
                    continue

                # Draw the star
                pygame.draw.circle(self.screen, self.WHITE, (int(x), int(y)), int(size))

                # Update star properties
                self.stars[i]=[x,y,size,dx,dy]
                
class GUI():
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200,720), pygame.RESIZABLE)
        pygame.display.set_caption('Task Assistant RPG')
        self.clock=pygame.time.Clock()
        self.currentframe=OpeningFrame(self.screen)
        self.currentframe._online=True
        self.running=True
        self.run()
    def run(self):
        while self.running:
            self.currentframe._readbuttoninput()
            self.currentframe._animate()
            pygame.display.flip()
            if self.currentframe._online==False:
                self.running=False
            # Cap the frame rate
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

if __name__ in "__main__":
    GUI()