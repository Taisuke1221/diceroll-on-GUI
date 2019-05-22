# making back system
#DICE ROLL
import random
#初期設定
sixsides = "0"
#6 face dice
sixsides =  random.randint(1,6)
print(sixsides)
tensides =  random.randint(1,10)
print(tensides)
twelsides = random.randint(1,12)
print(twelsides)

import tkinter as tk
#ウィンドウのサイズなど設定
root = tk.Tk()
root.title("DiceRoll")
root.geometry("640x480")






root.mainloop()
