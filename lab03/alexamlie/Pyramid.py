#Pyramid.py
#Alex Amlie-Wolf
#1-14-11
#A program to make a pyramid of bricks. I am testing Tkinters image capabilities

from Tkinter import *

class GUI(Frame):
    def __init__(self):
        Frame.__init__(self, None)
        self.grid()

        MenuBar = Frame(self)
        MenuBar.grid(row = 0, column = 0, sticky=W)

        QuitButton = Button(MenuBar, text="Quit", command = self.quit)
        QuitButton.grid(row=0, column=0)

        global canvas
        canvas = Canvas(self, width=600, height=800, background="cyan")
        canvas.grid(row=1, column=0)

def Rectangle(x0, y0, x1, y1, color):
    canvas.create_rectangle(x0, y0, x1, y1, fill=color)

def main():
    window = GUI()
    
    bricks = input("How many bricks do you want? ")
    width = 600
    height = 800
    for y in range(bricks):
        for x in range(bricks - y, 0, -1):
            xStart = width - x*(width/bricks) - y*(width/(2*bricks))
            yStart = height - y*(height/bricks)
            #print xStart,      I used these to check the starting coordinates
            #print yStart
            Rectangle(xStart, yStart-(height/bricks), xStart+(width/bricks), yStart, "yellow")
            
    window.mainloop()
            
main()
