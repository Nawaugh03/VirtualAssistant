
import time


import random
#import os
import math
#import random
import tkinter as tk

class Node:
    def __init__(self, canvas,x,y,size,color,SetColors):
        #when created the node will be assign valhes such as a sense of direction, its max size, min size, color, and set actions
        #the node will spawn on set canvas and positioned, colored, and sized properly
        self.canvas=canvas
        self.x=x
        self.y=y
        self.Originalsize=size
        self.minimumsize=self.Originalsize-19
        self.maximumsize=self.Originalsize+10
        self.direction=1
        self.currentsize=self.minimumsize
        self.alternatecolors=SetColors
        self.color=color
        self.square=None
        #All idle animations are turned off
        self.isfloating=False
        self.ispulsing=False
        self.isidle=False
        self.increase=False
        self.isgrowing=False
        self.isspinning=False
        self.iscentered=False
        self.snowflakes=[]
        self.isAnimating=False
        self.spawnNodeAnimation()

    def draw(self, initialsize):
        # Draw the square on the canvas
        x1 = self.x - initialsize // 2
        y1 = self.y - initialsize // 2
        x2 = self.x + initialsize // 2
        y2 = self.y + initialsize // 2
        self.square = self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.color, fill=self.color)
    def floating(self,t=0, amplitude=50, step_size=0.11):
        #The algorithm where the square is floating on the y axis
        y= y_center + amplitude *math.sin(t)
        self.canvas.coords(self.square, (self.canvas.winfo_reqwidth() // 2)-self.currentsize, y-self.currentsize, (self.canvas.winfo_reqwidth() // 2) + self.currentsize, y + self.currentsize)
        t+=step_size
        if(self.isfloating):
            self.canvas.after(45, self.floating,t, amplitude, step_size)

    def spinningIdle(self,spiral_radius,angle):
        #Node will gradually spin. Until it reaches the a maximum radiusm and it is stil spining but in a circle, if it stop spinning the node will gradually decrease its radius 
        spiral_angular_speed = 5
        spiral_radius_increment = 1
        x_spiral =(self.canvas.winfo_reqwidth() // 2) + int(spiral_radius * math.cos(math.radians(angle)))
        y_spiral = (self.canvas.winfo_reqheight() // 2) + int(spiral_radius * math.sin(math.radians(angle)))
        self.canvas.coords(self.square, x_spiral - self.currentsize, y_spiral - self.currentsize, x_spiral + self.currentsize, y_spiral + self.currentsize)
        angle += spiral_angular_speed
        if (spiral_radius<200 and self.increase):
            spiral_radius += spiral_radius_increment
        elif(spiral_radius>0 and self.increase == False):
            spiral_radius -= spiral_radius_increment
        
        """
        if(self.maxIdleTime==int(time.time()-self.timer)):
            self.increase=False
            self.timer=time.time()
        if(spiral_radius==0 and self.increase is False):
            self.isidle=False
            self.timer=0
        """
        #print("is spinning")
        if(self.isspinning==True):
            #print("is spinning")
            self.canvas.after(30,self.spinningIdle,spiral_radius, angle)  
        if(spiral_radius<=0):
            self.isspinning=False
        if(not self.isidle):
            self.reset(0)
           

    def boundaryIdle(self,x_speed, y_speed):
        #This animation is the DvD boundary idle animation
        current_coords=self.canvas.coords(self.square)
        new_x1 = current_coords[0] + x_speed
        new_y1 = current_coords[1] + y_speed
        new_x2 = current_coords[2] + x_speed
        new_y2 = current_coords[3] + y_speed
        if new_x1 <= 0 or new_x2 >= self.canvas.winfo_reqwidth():
            x_speed = -x_speed  # Reverse the horizontal direction
            new_color=random.choice(self.alternatecolors)
            self.canvas.itemconfig(self.square, fill=new_color, outline=new_color)
        if new_y1 <= 0 or new_y2 >= self.canvas.winfo_reqheight():
            y_speed = -y_speed  # Reverse the vertical direction
            new_color=random.choice(self.alternatecolors)
            self.canvas.itemconfig(self.square, fill=new_color, outline=new_color)
        self.canvas.move(self.square,x_speed,y_speed)
        #if (self.maxIdleTime==int(time.time()-self.timer)):
        #    self.isidle=False
        #    self.setToCenter(1)
        if(self.isidle):
            self.canvas.after(10, self.boundaryIdle, x_speed,y_speed)
        else:
            self.reset(1)
            return
            

    def spawnNodeAnimation(self):
        #have the node grow to its max size when spawning
        self.draw(self.currentsize)
        self.canvas.after(275, self.grow_node,self.Originalsize,15)

    def setToCenter(self,steps=15):
        #When this is called any animations will stop and set to center
        coordinates=self.canvas.coords(self.square)
        x1,y1,x2,y2=coordinates
        
        current_centerx=(x1+x2)/2
        current_centery=(y1+y2)/2
       
        dx=((self.canvas.winfo_reqwidth() // 2)-current_centerx)/steps
        dy=((self.canvas.winfo_reqheight() // 2)-current_centery)/steps
       
        if (abs(dx) <= 0.1 and abs(dy) <= 0.1):
            return
        
    
        self.canvas.move(self.square,dx,dy)  
        self.canvas.after(steps, self.setToCenter, steps)
       
    def resetSize(self):
        #Any growth or shrink in a size will reset to its original size
        if(self.Originalsize != self.currentsize):
            if(self.currentsize>self.Originalsize):
                self.currentsize-=1
            elif(self.currentsize<self.Originalsize):
                self.currentsize+=1
            self.canvas.coords(self.square, self.x-self.currentsize, self.y-self.currentsize, self.x+self.currentsize, self.y+self.currentsize)
            self.canvas.after(15, self.resetSize)   
        else:
            return
    def pulsing(self,maxsize,delay):
        #A pulsing animation where the node increase and decrease
        maxaura=maxsize
        delay=delay
        if(self.isidle): 
            if(self.isgrowing):
                self.grow_node(maxaura, delay=delay)
            else:
                self.shrink_node(self.Originalsize, delay=delay)
            self.canvas.after(delay,self.pulsing,maxsize,delay)
        else:
            self.reset(2)
            return
        
    def grow_node(self,target,delay):
        #The current size will start growing every 0.5 pixels per delay
        self.currentsize+=0.5
        #canvas.coords(self.square, self.x-self.currentsize, self.y-self.currentsize, self.x+self.currentsize, self.y+self.currentsize)
        if self.currentsize <  target:
            self.canvas.coords(self.square, self.x-self.currentsize, self.y-self.currentsize, self.x+self.currentsize, self.y+self.currentsize)
            self.canvas.after(delay,self.grow_node,target,delay)
        else:
            self.isgrowing=False
            return
    def shrink_node(self, target, delay):
        #The current size will start shrinking every 0.5 pixels per delay
        self.currentsize -= 0.5
        if self.currentsize > target:
            self.canvas.coords(self.square, self.x - self.currentsize, self.y - self.currentsize, self.x + self.currentsize, self.y + self.currentsize)
            self.canvas.after(delay, self.shrink_node,target,delay)
        else:
            self.isgrowing=True
            return
            
    def figureEight(self, angle, angle_increment):
        #This is an idle animation where the node will move in a figure eight
        #current_coords=self.canvas.coords(self.square)
        x = self.canvas.winfo_reqwidth() // 2 + (self.canvas.winfo_reqwidth() // 3) * math.cos(angle)
        y = self.canvas.winfo_reqheight() // 2 + (self.canvas.winfo_reqheight() // 5) * math.sin(2 * angle)
        
        self.canvas.coords(self.square, x - self.currentsize, y - self.currentsize, x + self.currentsize, y + self.currentsize)
        
        angle += angle_increment        
        if angle >= 2 * math.pi:
            angle = 0
        if(self.isidle):
            self.canvas.after(30, self.figureEight, angle, angle_increment)
        else:
            self.reset(3)
            return
    def change_color(self, current_color, target_color, steps, current_step):
        #change the color of the node
        # Convert the current color to RGB values
        current_r = int(current_color[1:3], 16)
        current_g = int(current_color[3:5], 16)
        current_b = int(current_color[5:7], 16)

        # Calculate the next intermediate color in hexadecimal format
        r1, g1, b1 = current_r, current_g, current_b
        r2, g2, b2 = int(target_color[1:3], 16), int(target_color[3:5], 16), int(target_color[5:7], 16)
        step = current_step / steps
        r = int(r1 + step * (r2 - r1))
        g = int(g1 + step * (g2 - g1))
        b = int(b1 + step * (b2 - b1))
        color_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)

        # Change the square's fill color
        self.canvas.itemconfig(self.square, fill=color_hex, outline=color_hex)

        # Increment the step counter
        current_step += 1

        # Schedule the next color change if not finished
        if current_step <= steps:
            self.canvas.after(steps, self.change_color,current_color, target_color, steps, current_step)

    def create_snowflake(self):
        x = random.randint(0, self.canvas.winfo_reqwidth())
        y = 0
        size = random.randint(5, 10)
        snowflake = self.canvas.create_oval(x, y, x + size, y + size, fill='white')
        self.snowflakes.append((snowflake, x, y, size))
        
        # Schedule the next snowflake creation
        if(self.isidle):
            self.canvas.after(random.randint(10, 50), self.create_snowflake)
        else:
            self.reset(4)
            return

    # Function to move the snowflakes
    def move_snowflakes(self):
        for i in range(len(self.snowflakes)):
            snowflake, x, y, size = self.snowflakes[i]
            self.canvas.move(snowflake, 0, 5)  # Increase the move distance to make it faster
            _, new_y1, _, new_y2 = self.canvas.coords(snowflake)
            
            # Remove snowflakes that go below the canvas
            if new_y2 >= self.canvas.winfo_reqheight():
                self.canvas.delete(snowflake)
                self.snowflakes[i] = (None, None, None, None)
        
        # Remove empty snowflake entries
        self.snowflakes[:] = [entry for entry in self.snowflakes if entry[0] is not None]
        
        # Schedule the next move
        if (not self.snowflakes):
            return
        else:
            self.canvas.after(50, self.move_snowflakes)  # Decrease the time interval to make it more frequent
    
    def idle(self, randomcode):
        #chose one of these idle animations and run it
        # 0 spinning idle
        # 1 corner idle including changing color
        # 2 pulsing animation
        # 3 figureeight animation
        # 4 start snowing animation
        self.isidle=True
        self.isAnimating=True
        if(randomcode==0):
            self.increase=True
            self.isspinning=True
            self.spinningIdle(0,0)
        elif(randomcode==1):
            self.boundaryIdle(3,2)
        elif(randomcode==2):
            self.isgrowing=True
            self.pulsing(maxsize=self.maximumsize+40, delay=40)
        elif(randomcode==3):
            self.figureEight(4.75,0.05)
        elif(randomcode==4):
            self.change_color(self.canvas.itemconfig(self.square, "fill")[4], "#00E1FF",30, 0)
            self.create_snowflake()
            self.move_snowflakes()
            
    
    def reset(self, randomnum):
        if(randomnum==0):
            self.increase=False
        if(randomnum==1):
            #print("Finish corner idle")
            self.canvas.itemconfig(self.square, fill=self.color, outline=self.color)
            self.setToCenter()
        if(randomnum==2):
            #print("Finish Pulse")
            self.resetSize()
        if(randomnum==3):
            #print("Finish figureEight")
            self.setToCenter()
        if(randomnum==4):
            self.change_color(self.canvas.itemconfig(self.square, "fill")[4], "#FF0000",30, 0)
        self.isAnimating=False
           
    

def changeBGcolor(canvas, current_color, target_color,delay, steps=100):
   # Function to fade the background color of a canvas from current_color to target_color
        r_step = (target_color[0] - current_color[0]) / steps
        g_step = (target_color[1] - current_color[1]) / steps
        b_step = (target_color[2] - current_color[2]) / steps
        
        def fade_color(step):
            if step <= steps:
                new_color = (
                    int(current_color[0] + r_step * step),
                    int(current_color[1] + g_step * step),
                    int(current_color[2] + b_step * step)
                )
                canvas.config(bg='#{:02x}{:02x}{:02x}'.format(*new_color))
                canvas.after(delay, fade_color, step + 1)
        
        fade_color(1)
def get_rgb_values(win,color):
     # Function to retrieve RGB values from a color string (e.g., "#RRGGBB")
        if color.startswith("#") and len(color) == 7:
            return tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
        else:
            # Invalid color format, return default black
            return (0, 0, 0)

def RuninBackGrounds(n):
    global startidleinverval, timer, chooseIdle, endidleinterval
    #currentBGcolor=get_rgb_values(canvas.cget("bg"))
    #target_color=[255,255,255]
    if(n is None):
        timer=time.time()
        n=Node(canvas=canvas, x=x_center, y=y_center, size=30, color="#FF0000", SetColors=["#00FF00","#0000FF","#FFFF00", "#FF9F00", "#00FFEB","#6AFF00"])
        n.spawnNodeAnimation()
        
    #changeBGcolor(canvas=canvas,)
    """
    if(startidleinverval==int(time.time()-timer) and n.isidle is False):
        chooseIdle = random.randint(0,4)
        #print("Starting IDle")
        n.idle(chooseIdle) 
        #n.isidle=True
        endidleinterval= 10
        timer=time.time()

        #timer=time.time()

    if(endidleinterval==int(time.time()-timer) and n.isidle):
        #print(chooseIdle)
        n.reset(chooseIdle)
        #print(n.isidle)
        #n.isidle=False
        timer=time.time()
    """
    if(startidleinverval==int(time.time()-timer)):
        n.changeBGcolor(n.canvas, get_rgb_values(win,n.canvas.cget("background")), (255,255,255),delay=5, steps=20)
        startidleinverval==0
    canvas.after(10,lambda:RuninBackGrounds(n))
if __name__ in "__main__":
    win = tk.Tk()
    win.title("Virtual Assistant")
    canvas=tk.Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight(), background="black")
    canvas.pack()
    x_center = canvas.winfo_reqwidth() // 2
    y_center =  canvas.winfo_reqheight() // 2
    n=None
    startidleinverval=10
    endidleinterval=random.randint(50,100)
    chooseIdle=0
    timer=0
   
    RuninBackGrounds(n)
    win.mainloop()


