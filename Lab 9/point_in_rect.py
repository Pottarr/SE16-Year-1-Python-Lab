from tkinter import *
import tkinter.messagebox
from random import *

class Main :
    def __init__(self) :
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 370, height = 220, bg = "white")
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.click)
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.create_rectangle(10,10,360,210)
        
    def click(self, event) :
        inside_rectangle = (event.x > 10 and event.x < 360) and (event.y > 10 and event.y < 210)
        r_code = randint(0,255)
        g_code = randint(0,255)
        b_code = randint(0,255)
        if inside_rectangle == True :
            self.canvas.create_oval(event.x -5, event.y - 5, event.x + 5, event.y + 5, fill = "#%02x%02x%02x" %(r_code, g_code, b_code), tags = "oval")
        else :
            tkinter.messagebox.showwarning("showwarning", "Mouse pointer is not in the rectangle.")
    
app = Main()
app.root.mainloop()