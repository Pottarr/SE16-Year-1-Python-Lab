from tkinter import *

class Main :
    def __init__(self) :
        self.root = Tk()
        self.drawing_canvas = Canvas(self.root, width = 500, height = 350, bg = "white")
        self.drawing_canvas.pack()
        self.drawing_canvas.bind("<B1-Motion>", self.draw)
        self.drawing_canvas.bind("<Button-1>", self.draw)
        self.instruction = Label(self.root, text = "Drag the mouse to draw")
        self.instruction.pack()
        self.clear_button = Button(self.root, text = "Clear", command = self.clear_canvas)
        self.clear_button.pack()
    
    def draw(self, event) :
        self.drawing_canvas.create_oval(event.x -5, event.y - 5, event.x + 5, event.y + 5, fill = "black", tags = "oval")
                
    def clear_canvas(self) :
        self.drawing_canvas.delete("oval")
        
app = Main()
app.root.mainloop()