from tkinter import *
import tkinter.messagebox

class Main :
    def __init__(self) :
        self.root = Tk()
        self.input_money_str = ""
        self.money_entry = Entry(self.root)
        self.money_entry.pack()
        self.usd_to_thb_button = Button(self.root, text = "USD -> THB", command = self.usd_to_thb)
        self.usd_to_thb_button.pack()
        self.thb_to_usd_button = Button(self.root, text = "THB -> USD", command = self.thb_to_usd)
        self.thb_to_usd_button.pack()
        
        
    def usd_to_thb(self) :
        money = float(self.money_entry.get())
        result = money * 30
        sentence = str(money) + "USD = " + str(result) + "THB."
        tkinter.messagebox.showinfo("showinfo", sentence)
    
    def thb_to_usd(self) :
        money = float(self.money_entry.get())
        result = money / 30
        sentence = str(money) + "THB = " + str(result) + "USD."
        tkinter.messagebox.showinfo("showinfo", sentence)
        
        
app = Main()

app.root.mainloop()