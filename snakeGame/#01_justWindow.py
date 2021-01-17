from tkinter import *

game_width = 500
game_height = 500

tk = Tk()
tk.title("Змейка")
tk.resizable(0, 0) # resizable(width False, height False)
tk.wm_attributes("-topmost", 1
                 # "-fullscreen", 0
                 )
canvas = Canvas(tk,
                width = game_width, 
                height = game_height,
                bd = 0,
                bg = "gray",
                highlightthickness = 0)
canvas.pack()
tk.update()

tk.mainloop()