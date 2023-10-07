import pygame
from pygame.locals import *
import time
from tkinter import *




def Animate(x1,y1,x2,y2,velocity, surface):

    #x1,y1 - line first point
    #x2, y2 - line last poit
    dx=abs(x2-x1) #abs-module delta x
    dy=abs(y2-y1) #abs-module delta y
    p=2*dy-dx
    surface.fill((255, 255, 255))
    if x1<x2: # x axis line orientation
        xs=1
    else:
        xs=-1
        
    if y1<y2: # y axis line orientation
        ys=1
    else:
        ys=-1
    
    
    x=x1 #first line point
    y=y1
    if dx>dy:
        
        while x!=x2: #until last point is reached
            x=x+xs
            if p>0:
                y=y+ys
                p=p+2*dy-2*dx
            else:
                p=p+2*dy
            time.sleep(velocity**-1)
            surface.fill((255, 255, 255))
            DrawLine(x1, y1, x2, y2, surface)
            pygame.draw.circle(surface, (255,0,0), (x,y), 12)
            pygame.display.update()
            
            
            
    else:
        
        while y!=y2: #until last point is reached
            y=y+ys
            if p>0:
                x=x+xs
                p=p+2*dx-2*dy
            else:
                p=p+2*dx
            time.sleep(velocity**-1)
            surface.fill((255, 255, 255))
            
            DrawLine(x1, y1, x2, y2, surface)
            pygame.draw.circle(surface, (255,0,0), (x,y), 12)
            pygame.display.update()

def DrawLine(x1,y1,x2,y2, surface):
    #x1,y1 - line first point
    #x2, y2 - line last poit
    dx=abs(x2-x1) #abs-module delta x
    dy=abs(y2-y1) #abs-module delta y
    p=2*dy-dx
    
    if x1<x2: # x axis line orientation
        xs=1
    else:
        xs=-1
        
    if y1<y2: # y axis line orientation
        ys=1
    else:
        ys=-1
    
    
    x=x1 #first line point
    y=y1
    if dx>dy:
        while x!=x2: #until last point is reached
            x=x+xs
            if p>0:
                y=y+ys
                p=p+2*dy-2*dx
            else:
                p=p+2*dy
            surface.set_at((x, y), (0,0,0))
            
            
            
    else:
        while y!=y2: #until last point is reached
            y=y+ys
            if p>0:
                x=x+xs
                p=p+2*dx-2*dy
            else:
                p=p+2*dx
            surface.set_at((x, y), (0,0,0))


def Animation(x1,y1,x2,y2,velocity, width, height):
    direction = True

    # Decide Width and Height of the window(600x600 is minimal)
    intendedWidth = max(width, 600)
    intendedHeight = max(height, 600)
    # Initiate pygame
    pygame.init()
    # Create Surface
    window = pygame.display.set_mode((intendedWidth, intendedHeight))
    window.fill((255,255,255))
    pygame.display.update()
    # Creating a new clock object to
    # track the amount of time
    clock = pygame.time.Clock()
    
    # Creating variable that
    # programm will use to run the while loop
    run = True

    # Creating an infinite loop
    while run:
        
        # Setting the framerate to 30fps 
        clock.tick(30)
        
        # Loop to exit the game if space is pressed
        for event in pygame.event.get():
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.display.quit()
                    pygame.quit()
                
        # if-else to swap the circle direction after animation ends       
        if direction == True:
            Animate(x1, y1, x2, y2,velocity,window)
            direction = False
        else:
            Animate(x2, y2, x1, y1,velocity,window)
            direction = True

# Animation
def StartAnimation():
    try:
        # Read the values inside entries
        x1 = int(my_boxx1.get())
        y1 = int(my_boxy1.get())
        x2 = int(my_boxx2.get())
        y2 = int(my_boxy2.get())
        velocity = int(my_boxVel.get())
        
        # Negative number check
        if velocity < 0 or x1 < 0 or x2 < 0  or y1 < 0 or y2 < 0:
            raise ValueError
        # equal points check
        if x1==x2 and y1==y2:
            raise ArithmeticError
        
        width = max(x1,x2)
        height = max(y1,y2)
        try:
            
            Animation(x1,y1,x2,y2,velocity, width, height)
            
        except pygame.error:
            #if animation is canceled
            my_labelError.config(text="Animation has ended")
        
    except ValueError:
        #if user inputed non-integer or negative numbers
        my_labelError.config(text="Please enter positive whole numbers")
    except ArithmeticError:
        #if user inputed equal points
        my_labelError.config(text="Please enter non-equal points")
# to close tkinter window
def Quit():
    window.destroy()
    
# Tkinter master
window = Tk()

# Master params
window.geometry("400x650")
window.title("Brezenhem Animation")

# Labels/Entries/Buttons
my_labelx1 = Label(window, text="Enter first point X coordinate").pack(pady=20)
my_boxx1 = Entry(window)
my_boxx1.pack(pady=3)

my_labely1 = Label(window, text="Enter first point Y coordinate").pack(pady=20)
my_boxy1 = Entry(window)
my_boxy1.pack(pady=3)

my_labelx2 = Label(window, text="Enter second point X coordinate").pack(pady=20)
my_boxx2 = Entry(window)
my_boxx2.pack(pady=3)

my_labely2 = Label(window, text="Enter second point Y coordinate").pack(pady=20)
my_boxy2 = Entry(window)
my_boxy2.pack(pady=3)

my_labelVel = Label(window, text="Enter velocity").pack(pady=20)
my_boxVel = Entry(window)
my_boxVel.pack(pady=10)

my_labelError = Label(window, text=" ")
my_labelError.pack(pady=30)

button = Button(window, text = "Start Animation",command=StartAnimation).pack()
quit_button = Button(window, text = "Quit",command=window.destroy).pack()

my_label = Label(window, text="To close animation press space")
my_label.pack(pady=30)

window.mainloop()

 
   