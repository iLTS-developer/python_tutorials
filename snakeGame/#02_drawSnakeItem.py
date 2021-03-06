from tkinter import *

game_width = 500
game_height = 500
snake_item = 20
snake_color1 = "red"
snake_color2 = "yellow"

gamesize_x = game_width // snake_item
gamesize_y = game_height // snake_item

snake_x = gamesize_x // 2
snake_y = gamesize_y // 2

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

def snake_paint_item(canvas, x, y):
    id1 = canvas.create_rectangle(x*snake_item,
                                  y*snake_item, 
                                  x*snake_item + snake_item,
                                  y*snake_item + snake_item,
                                  fill = snake_color2)
    id2 = canvas.create_rectangle(x*snake_item + 2,
                                  y*snake_item + 2,
                                  x*snake_item + snake_item - 2,
                                  y*snake_item + snake_item - 2,
                                  fill = snake_color1)
    
snake_paint_item(canvas, snake_x, snake_y)


tk.mainloop()