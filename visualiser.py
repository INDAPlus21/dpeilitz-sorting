#code greatly inspired by https://python.plainenglish.io/build-a-sorting-algorithm-visualizer-in-python-f6f4afb1c98a
from tkinter import *
from tkinter import ttk

import random


#colors
BLACK = "#000000"
WHITE = "#FFFFFF"
GREY = "#555555"

window = Tk()
window.title("sort")
window.maxsize(1920,1080)
window.minsize(700,400)
window.config(bg = WHITE)



# generate an array of random values
def draw(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

def generate():
    
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    draw(data, [BLACK for x in range(len(data))])

# set the speed of the sorting process
def set_speed(speed):
    pass

# sorting!
def sort():
    pass

### USER INTERFACE ###
UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=1, column=0)

## Dropdown menu for algoritm

## BUTTONS :D
# sort
sort_btn = Button(UI_frame, text="Sortera", command=sort, bg = WHITE)
sort_btn.grid(row=2, column=1, padx=5, pady=5)

# generate new values into the array
gen_btn = Button(UI_frame, text="Generera", command=generate, bg= WHITE, border = 0)
gen_btn.grid(row=2, column=0, padx=5, pady=5)


## entry fields
# amount of elements to be sorted
amount = Label(UI_frame, text = "Antal element", fg = BLACK, background= WHITE)
amount.grid(row = 2, column =3)
e1 = Entry(UI_frame)
e1.grid(row= 2, column = 4)

#Canvas to draw the elements upon
canvas = Canvas(window, width= 800, height= 400, bg = WHITE, border = 0)
canvas.grid(row=0, column=0, padx=10, pady=5)

### end of USER INTERFACE ###

window.mainloop()