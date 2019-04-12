from Tkinter import *
from PIL import Image, ImageTk

class Application(Frame):
    
    def start(self):
        print "Please remain some moments still"
        
    def select(self, v):
        if(self.var.get() == "Archer"):
            self.source = "./images/archery.jpg"
        elif(self.var.get() == "Vrkasana"):
            self.source = "./images/vrkasana.jpg"
        elif(self.var.get() == "Squats"):
            self.source = "./images/squats.jpg"
        self.image2 = Image.open(self.source)
        self.image = self.image2.resize((350, 500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)

        self.label.configure(image=self.photo)
        self.label.image = self.photo


    def createWidgets(self):
        frametop = Frame(root)
        frametop.pack(side=TOP, fill=BOTH, expand=1)

        self.var = StringVar(self)
        self.var.set("Select your pose") # initial information
        self.option = OptionMenu(frametop, self.var, "Archer", "Vrkasana", "Squats",  command = self.select)
        self.option.pack({"side": "left"})

        self.QUIT = Button(frametop)
        self.QUIT["text"] = "FINISH"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "right"})

        self.START = Button(frametop)
        self.START["text"] = "START"
        self.START["command"] = self.start
        
        self.START.pack({"side": "right"})
        
        self.source_v = "./images/white.jpg"

        self.image_v = Image.open(self.source_v)
        self.image_v = self.image_v.resize((350, 500), Image.ANTIALIAS)
        self.photo_v = ImageTk.PhotoImage(self.image_v)

        self.label_v = Label(image=self.photo_v)
        self.label_v.image = self.photo_v
        self.label_v.pack({"side": "right"})
        
        self.source = "./images/white.jpg"

        self.image = Image.open(self.source)
        self.image = self.image.resize((350, 500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = Label(image=self.photo)
        self.label.image = self.photo
        self.label.pack({"side": "right"})


        


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
