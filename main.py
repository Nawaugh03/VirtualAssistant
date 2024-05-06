import VAGui
from VAGui import *
from VAListenSystem import ListenSystem
from VAListenSystem import sr
import threading
"""
The main function allows the VA's Listen System and the GUI to interact wirh each other
Add Personalization for AI generated prompts
giving this VA an Identity
"""

class Controller:
    def __init__(self):
        self.online=False
        self.name="test"
        self.startidleinverval=10
        self.endidleinterval=random.randint(50,100)
        self.chooseIdle=0
        self.activityInterval=5
        self.activityTimer=updatetimer()
        self.timer=updatetimer()
        self.Nodeactivity=False
        self.isAwake=False
        self.isSpeaking=True
        self.introduction=False
        self.isAnimating=False
        self.counter=0

def updatetimer():
    return time.time()
controller=Controller()

def RuninBackGrounds(win):
    #currentBGcolor=get_rgb_values(canvas.cget("bg"))
    #target_color=[255,255,255]
    #If the node is inactive the bg will fade to black and the node will do its idle animations
    controller.isAnimating=n.isAnimating
    if(controller.Nodeactivity==False):
        if controller.isAwake:
            controller.isAwake=False
            #print("sleeping")
            controller.introduction=False
            n.isidle=False
        VAGui.changeBGcolor(canvas=n.canvas,current_color=VAGui.get_rgb_values(win,n.canvas.cget("background")) ,target_color=(0,0,0),delay=5, steps=40)
        #controller.activityTimer=updatetimer()
        if(controller.startidleinverval==int(time.time()-controller.timer) and n.isidle is False):
                controller.chooseIdle=random.randint(0,4)
                n.idle(controller.chooseIdle)
                controller.isAnimating=True
                #endidleinterval= 10
                controller.timer=updatetimer()
        if(controller.endidleinterval==int(time.time()-controller.timer) and n.isidle):
                n.isidle=False
                controller.timer=updatetimer()

    if(controller.Nodeactivity==True):
        VAGui.changeBGcolor(canvas=n.canvas,current_color=VAGui.get_rgb_values(win,n.canvas.cget("background")) ,target_color=(255,255,255),delay=5, steps=40)
        if controller.isAwake==False:
            controller.isAwake=True
            #print("Im up")
            controller.activityTimer=updatetimer()
            n.isidle=False

        
        #This piece of code set the node activity to false within the activity timer
        #if (controller.activityInterval==int(time.time()-controller.activityTimer)):
        #    controller.Nodeactivity=False
        #    controller.activityTimer=updatetimer()

        #if (n.isAnimating==False):
        #    if (controller.isSpeaking==True and controller.counter==0):
        #        controller.chooseIdle=2
        #        controller.counter+=1
        #        n.idle(controller.chooseIdle)
        #    elif(controller.isSpeaking==False and controller.counter==1):
        #        controller.counter-=1
        #        n.isidle=False
        
        
        """
        if controller.isSpeaking==True and controller.isAnimating==False and controller.counter==0:
            controller.chooseIdle=2
            controller.isAnimating=True
            controller.coutner=1
            n.idle(controller.chooseIdle)
        if controller.isSpeaking==False and controller.isAnimating=True:
            controller.working=False
            n.isidle=False
        """
        
   

    if win.winfo_exists():
        controller.online=True
        canvas.after(10,lambda:RuninBackGrounds(win))
    else:
        controller.online=False



def listening():
    LS=ListenSystem()
    ResponseTimeWindow=0
    while controller.online==True:
        LS.takeCommand()
        if controller.name in LS.query():
            controller.Nodeactivity=True
            LS.intro()
            LS.takeCommand()
            if LS.query != "None":
                LS.process_action()
            else:
                controller.Nodeactivity=False

        
def on_click(event): 
    if(controller.Nodeactivity==True):
        controller.Nodeactivity=False
        controller.timer=updatetimer()
    else: 
        controller.Nodeactivity=True
  

def start_speech_recognition():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for speech...")
        while True:
            print("Yep")
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                print("Recognized:", text)
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print("Error fetching results; {0}".format(e))
            
# Create the thread for the background task

if __name__ in '__main__':
    controller.online=True
    controller.isAwake=False
    background_thread = threading.Thread(target=listening)
    background_thread.daemon = True  # Daemonize the thread so it automatically exits when the main program ends
    background_thread.start()
    win = tk.Tk()
    win.title("Virtual Assistant")
    canvas=tk.Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight(), background="black")
    canvas.pack()
    x_center = canvas.winfo_reqwidth() // 2
    y_center =  canvas.winfo_reqheight() // 2  
    n=Node(canvas=canvas, x=x_center, y=y_center, size=30, color="#FF0000", SetColors=["#00FF00","#0000FF","#FFFF00", "#FF9F00", "#00FFEB","#6AFF00"])
    #Test Alternate functions when clicking the VA
    #win.bind("<Button-1>", on_click)
    #ui_thread=threading.Thread(target=RuninBackGrounds, args=win)
    #ui_thread.daemon=True
    #ui_thread.start()
    RuninBackGrounds(win)
    win.mainloop()
    #background_thread.join()
    