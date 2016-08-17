import time
from tkinter import *

root = Tk()
frame = Frame(root, height = 532, width = 532)
frame.pack()
    
screen = Canvas(frame, bg = "black")
screen.pack()
screen.place(x =10 , y =10 , height = 512, width = 512)

for i in range(32):
	screen.create_rectangle(0+(i*16), 0, 16+(i*16), 16, fill='red')
	root.update()
	time.sleep(0.5)
