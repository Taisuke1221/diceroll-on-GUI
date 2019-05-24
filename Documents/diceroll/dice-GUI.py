import tkinter as tk

root = tk.Tk()

root.geometry("640x480")
#generate Frame
FrameSides = tk.Frame(root)
FrameText  = tk.Frame(root)
FrameOpt   = tk.Frame(root)

class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)#, height = 640, width = 480)
        self.place()
        self.createlabel()
        self.createbutton()
        self.createlogwindow()

    #def createWidgets(self):
    #    self.quitbutton = tk.Button(self, text = "Quit", command = self.quit)
    #    self.quitbutton.grid()


    def createlabel(self):
        tk.Label(FrameSides,text = "choose DiceSides number.")#.place(height = 50, width = 10)
        tk.Label(FrameText,text = "logs'll delete with closing window.")#.place(height = 10, width = 200)

    def createbutton(self):
        self.SixSidesButton     = tk.Button(FrameSides, text = "1-6")#.place(height = 50, width = 100)   #1
        self.TenSidesButton     = tk.Button(FrameSides, text = "1-10")#.place(height = 50, width = 190)  #2
        self.TwelveSidesButton  = tk.Button(FrameSides, text = "1-12")#.place(height = 50, width = 280)  #3
        self.HundredSidesButton = tk.Button(FrameSides, text = "1-100")#.place(height = 50, width = 370) #4
        self.FavsidesButton     = tk.Button(FrameSides, text = "Dice")#.place(height = 50, width = 450) #5

    def createlogwindow(self):
        self.logwindow = tk.Text(FrameText,height = 20, width = 20, wrap = tk.CHAR)#.place(height = 9, width = 18)

#SetFrame
FrameSides.grid()
FrameText.grid()
FrameOpt.grid()

app = Application()
app.master.title("diceroll application")

app.mainloop()