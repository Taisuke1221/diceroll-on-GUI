mport tkinter as tk

root = tk.Tk()

root.geometry("640x480")

class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitbutton = tk.Button(self, text = "Quit", command = self.quit)
        self.quitbutton.grid()

app = Application()
app.master.title("diceroll application")

app.mainloop()