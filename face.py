from Tkinter import *
from colors import BMO_FACE

WINDOW_W = 500
WINDOW_H = 350

def createDisplay():
    global tk
    tk = Tk()
    canvas = Canvas(tk, bg=BMO_FACE, width=WINDOW_W, height=WINDOW_H)
    canvas.create_oval(100,50,150,100, fill='black')
    canvas.create_oval(300,50,350,100, fill='black')
    canvas.pack()
    tk.mainloop()
    
def main():
    createDisplay()

if __name__ == '__main__':
    main()