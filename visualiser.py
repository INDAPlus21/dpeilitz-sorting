# code greatly inspired by https://python.plainenglish.io/build-a-sorting-algorithm-visualizer-in-python-f6f4afb1c98a
from tkinter import *
from tkinter import ttk
from bubble import bubble_sort

import random


# colors
BLACK = "#000000"
WHITE = "#FFFFFF"
GREY = "#555555"

window = Tk()
window.title("sort")
window.maxsize(1920, 1080)
window.minsize(700, 400)
window.config(bg=WHITE)

# canvas height and width
c_height = 400
c_width = 800

global data
num = 100
# generate an array of random values

algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Merge Sort']


def draw(dataArray):
    canvas.delete("all")
    x_width = c_width / len(dataArray)
    for i in range(0, len(dataArray)):
        x0 = i * x_width
        y0 = c_height - dataArray[i]
        x1 = (i + 1) * x_width
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=WHITE)

    window.update_idletasks()


def generate():
    global data
    data = []

    input = int(e1.get())
    # KAn behöva fixa detta, den ger error vid strings. Ah well
    # Create as many elements as can fit inside of the window
    for i in range(0, input):
        data.append(random.randint(1, c_height))
    draw(data)

# set the speed of the sorting process

# sorting!


def sort():
    global data
    #timeTick = set_speed()
    bubble_sort(data, draw)


### USER INTERFACE ###
UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=1, column=0)

# Dropdown menu for algoritm
l1 = Label(UI_frame, text="Algoritm: ", bg=WHITE)
l1.grid(row=2, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(
    UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=2, column=1, padx=5, pady=5)
algo_menu.current(0)

# BUTTONS :D
# generate new values into the array
gen_btn = Button(UI_frame, text="Generera", command=generate, bg=WHITE)
gen_btn.grid(row=2, column=2, padx=5, pady=5)
# sort
sort_btn = Button(UI_frame, text="Sortera", command=sort, bg=WHITE)
sort_btn.grid(row=2, column=3, padx=5, pady=5)


# entry fields
# amount of elements to be sorted
amount = Label(UI_frame, text="Antal element", fg=BLACK, background=WHITE)
amount.grid(row=2, column=4)
e1 = Entry(UI_frame)
e1.insert(END, "50")
e1.grid(row=2, column=4)

# Canvas to draw the elements upon
canvas = Canvas(window, width=c_width,
                height=c_height, bg=BLACK, border=0)
canvas.grid(row=0, column=0, padx=10, pady=5)

### end of USER INTERFACE ###

window.mainloop()
