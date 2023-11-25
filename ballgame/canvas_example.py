import tkinter

oval_id = None


def create_ball():
    global oval_id
    if oval_id is None:
        oval_id = canvas.create_oval(10, 10, 20, 20, fill="red")
    else:
        print("Oval is already made")

def delete_ball():
    global oval_id
    canvas.delete(oval_id)
    oval_id = None


def click_handler(event):
    print(event.x, event.y)
    if oval_id is not None:
        canvas.coords(oval_id, (event.x-5, event.y-5, event.x+5, event.y+5))

root = tkinter.Tk("Main window")
root.geometry("640x480")


buttons_panel = tkinter.Frame(bg="red", width="640")
button_start = tkinter.Button(buttons_panel, text="Start", command=create_ball)
button_start.pack(side=tkinter.LEFT)
button_stop = tkinter.Button(buttons_panel, text="Stop", command=delete_ball)
button_stop.pack(side=tkinter.LEFT)
buttons_panel.pack(side=tkinter.TOP, anchor="nw")

canvas = tkinter.Canvas(root, bg="lightgrey")
canvas.pack(side=tkinter.TOP, anchor="nw", fill=tkinter.X)
canvas.bind("<Button>", click_handler)

root.mainloop()