from tkinter import *
from client import *


class Controller:
    def __init__(self):
        self.window = App(self)
        self.client = Client()
        self.client.observer  = self

    def showFrame(self, frame_id):
        self.window.showFrame(frame_id)
    
    def sendMessage(self, msg):
        self.client.sendMessage(msg)
        # self.getMessage()
    
    def getMessage(self):
        msg = self.client.getMessage()
        self.window.chat_frame.showMessage(msg)

    def message_received(self, msg):
        self.window.chat_frame.showMessage(msg)


class App(Tk):
    def __init__(self, controller):
        super(App, self).__init__()
        
        self.controller = controller

        self.cont = Frame(self)
        self.cont.pack()
        self.cont.rowconfigure(0, weight=1)
        self.cont.columnconfigure(0, weight=1)

        self.geometry("400x400")

        self.intro_frame = IntroFrame(self.cont, self.controller)
        self.intro_frame.grid(row=0, column=0, sticky="nsew")
        
        self.chat_frame = ChatFrame(self.cont, self.controller)
        self.chat_frame.grid(row=0, column=0, sticky="nsew")
        
        self.intro_frame.tkraise()
    
    def showFrame(self, frame_id):
        if frame_id == 0:
            self.intro_frame.tkraise()
        elif frame_id == 1:
            self.chat_frame.tkraise()


class IntroFrame(Frame):
    def __init__(self, parent, controller: Controller):
        super(IntroFrame, self).__init__(parent)
        self.controller = controller
        
        label = Label(self, text="Insert Message")
        label.pack()
        
        self.msg = StringVar()
        entry = Entry(self, textvariable=self.msg)
        entry.pack()

        button = Button(self, text="Submit", command=self.sendMessage)
        button.pack()

    def sendMessage(self):        
        self.controller.sendMessage(self.msg.get())
        controller.showFrame(1)
    

class ChatFrame(Frame):
    def __init__(self, parent, controller: Controller):
        super(ChatFrame, self).__init__(parent)
        self.controller = controller

        self.listbox = Listbox(self, width=100)

        self.listbox.pack()
    
    def showMessage(self, msg):
        print(msg)
        self.listbox.insert(1, msg)
        self.listbox.pack()

        
if __name__ == "__main__":
    controller = Controller()
    controller.window.mainloop()