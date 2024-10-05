from tkinter import *

class Main :
    def __init__(self) :
        self.root = Tk()
        self.root.title("tk")
        self.root.geometry("1280x720")
        self.canvas = Canvas(self.root, width = 1280, height = 720, bg = "white")
        self.canvas.pack()
        self.circle_id = 0
        self.circle_list = []
        self.canvas.bind("<B1-Motion>", self.create_circle)
        self.canvas.bind("<Button-1>", self.create_circle)
        self.canvas.bind("<B3-Motion>", self.destroy_circle)
        self.canvas.bind("<Button-3>", self.destroy_circle)

    def create_circle(self, event) :
        circle_name = "circle" + str(self.circle_id)
        self.canvas.create_oval(event.x - 50, event.y - 50, event.x + 50, event.y + 50, tag = circle_name)
        self.circle_list.append([event.x, event.y])
        self.circle_id += 1
        
    def destroy_circle(self, event) :
        for i in range(len(self.circle_list)) :
            distance = ((self.circle_list[i][0] - event.x) ** 2 + (self.circle_list[i][1] - event.y) ** 2) ** 0.5
            if distance <= 50 :
                circle_name = "circle" + str(i)
                self.canvas.delete(circle_name)
            else :
                pass
app = Main()
app.root.mainloop()