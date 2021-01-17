from tkinter import *

game_width = 500
game_height = 500
snake_item = 20
snake_color1 = "red"
snake_color2 = "yellow"

gamesize_x = game_width // snake_item
gamesize_y = game_height // snake_item

snake_x = gamesize_x//2 + 1
snake_y = gamesize_y//2

snake_x_dir = 1
snake_y_dir = 0

snake_list = []

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

def snake_DrawItem(canvas, x, y):
    global snake_list
    id1 = canvas.create_rectangle(x*snake_item,
                                  y*snake_item, 
                                  x*snake_item+snake_item,
                                  y*snake_item+snake_item,
                                  fill=snake_color2)
    id2 = canvas.create_rectangle(x*snake_item+2,
                                  y*snake_item+2,
                                  x*snake_item+snake_item-2,
                                  y*snake_item+snake_item-2,
                                  fill=snake_color1)
    snake_list.append([id1, id2])
    
snake_DrawItem(canvas, snake_x - 2, snake_y)
snake_DrawItem(canvas, snake_x - 1, snake_y)
snake_DrawItem(canvas, snake_x, snake_y)

def snake_move(event):
    global snake_x
    global snake_y
    global snake_x_dir
    global snake_y_dir
    
    if ((event.keysym == "Up") and 
        not ((snake_x_dir == 0) and (snake_y_dir == 1))):
        snake_x_dir = 0
        snake_y_dir = -1
        
    elif ((event.keysym == "Down") and 
          not ((snake_x_dir == 0) and (snake_y_dir == -1))):
        snake_x_dir = 0
        snake_y_dir = 1
        
    elif ((event.keysym == "Left") and 
          not ((snake_x_dir == 1) and (snake_y_dir == 0))):
        snake_x_dir = -1
        snake_y_dir = 0
        
    elif ((event.keysym == "Right") and
          not ((snake_x_dir == -1) and (snake_y_dir == 0))):
        snake_x_dir = 1
        snake_y_dir = 0
        
    canvas.delete(snake_list[0][0], snake_list[0][1])
    snake_list.pop(0)    
    
    snake_x = snake_x + snake_x_dir
    snake_y = snake_y + snake_y_dir
    snake_DrawItem(canvas, snake_x, snake_y)
    
canvas.bind_all("<KeyPress-Left>", snake_move)
canvas.bind_all("<KeyPress-Right>", snake_move)
canvas.bind_all("<KeyPress-Up>", snake_move)
canvas.bind_all("<KeyPress-Down>", snake_move)




tk.mainloop()