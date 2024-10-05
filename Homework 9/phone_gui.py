from tkinter import *

class Main :
    def __init__(self) :
        self.root = Tk()
        self.root.title("KMITL Phone")
        self.root.geometry("300x300")
        self.root.grid_columnconfigure(0, weight = 1)
        self.root.grid_rowconfigure((0, 1, 2), weight = 1)
        
        self.num_pressed_text = StringVar()
        self.num_pressed_display = Label(self.root, textvariable = self.num_pressed_text)
        self.num_pressed_display.grid(row = 0, column = 0, sticky = "nsew")
        
        self.input_button_frame = Frame(self.root)
        self.input_button_frame.grid(row = 1, column = 0, sticky = "nsew")
        self.input_button_frame.grid_columnconfigure((0, 1, 2), weight = 1)
        self.input_button_frame.grid_rowconfigure((0, 1, 2, 3), weight = 1)
    
        self.num_1_button = Button(self.input_button_frame, text = "1", command = lambda : self.pressed_input_button("1"))
        self.num_1_button.grid(row = 0, column = 0, sticky = "nsew")
        
        self.num_2_button = Button(self.input_button_frame, text = "2", command = lambda : self.pressed_input_button("2"))
        self.num_2_button.grid(row = 0, column = 1, sticky = "nsew")
        
        self.num_3_button = Button(self.input_button_frame, text = "3", command = lambda : self.pressed_input_button("3"))
        self.num_3_button.grid(row = 0, column = 2, sticky = "nsew")
        
        self.num_4_button = Button(self.input_button_frame, text = "4", command = lambda : self.pressed_input_button("4"))
        self.num_4_button.grid(row = 1, column = 0, sticky = "nsew")
        
        self.num_5_button = Button(self.input_button_frame, text = "5", command = lambda : self.pressed_input_button("5"))
        self.num_5_button.grid(row = 1, column = 1, sticky = "nsew")
        
        self.num_6_button = Button(self.input_button_frame, text = "1", command = lambda : self.pressed_input_button("6"))
        self.num_6_button.grid(row = 1, column = 2, sticky = "nsew")
        
        self.num_7_button = Button(self.input_button_frame, text = "7", command = lambda : self.pressed_input_button("7"))
        self.num_7_button.grid(row = 2, column = 0, sticky = "nsew")
        
        self.num_8_button = Button(self.input_button_frame, text = "8", command = lambda : self.pressed_input_button("8"))
        self.num_8_button.grid(row = 2, column = 1, sticky = "nsew")
        
        self.num_9_button = Button(self.input_button_frame, text = "9", command = lambda : self.pressed_input_button("9"))
        self.num_9_button.grid(row = 2, column = 2, sticky = "nsew")
        
        self.asterisk_button = Button(self.input_button_frame, text = "*", command = lambda : self.pressed_input_button("*"))
        self.asterisk_button.grid(row = 3, column = 0, sticky = "nsew")
        
        self.num_0_button = Button(self.input_button_frame, text = "0", command = lambda : self.pressed_input_button("0"))
        self.num_0_button.grid(row =  3, column = 1, sticky = "nsew")
        
        self.hash_button = Button(self.input_button_frame, text = "#", command = lambda : self.pressed_input_button("#"))
        self.hash_button.grid(row = 3, column = 2, sticky = "nsew")
        
        self.action_button_frame = Frame(self.root)
        self.action_button_frame.grid_columnconfigure((0, 1), weight = 1)
        self.action_button_frame.grid_rowconfigure(0, weight = 1)
        self.action_button_frame.grid(row = 2, column = 0, sticky = "nsew")
        
        self.talk_button = Button(self.action_button_frame, text = "Talk", command = self.pressed_talk_button)
        self.talk_button.grid(row = 0, column = 0, sticky = "nsew")
        
        self.delete_button = Button(self.action_button_frame, text = "<", command = self.pressed_delete_button)
        self.delete_button.grid(row = 0, column = 1, sticky = "nsew")
        
    def pressed_input_button(self, character) :
        current_value = self.num_pressed_text.get()
        self.num_pressed_text.set(current_value + character)
        
    def pressed_talk_button(self) :
        phone_num = self.num_pressed_text.get()
        calling_msg = "Dialing<<" + phone_num + ">>"
        if "Dialing<<" not in self.num_pressed_display["text"] :
            self.num_pressed_text.set(calling_msg)
        else :
            pass
        
    def pressed_delete_button(self) :
        current_value = self.num_pressed_text.get()
        if len(current_value) > 0 :
            deleted_last_num = current_value[:-1]
            self.num_pressed_text.set(deleted_last_num)
        else :
            pass

        
app = Main()
app.root.mainloop()