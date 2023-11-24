import tkinter


def hello():
    print("Hello, world!")


def bye():
    print('Good bye')


root = tkinter.Tk()


root.bind("<Key>", hello)
button1 = tkinter.Button(master=root, text="hello")
button1.pack()
button1['command'] = hello

root.bind('<Key>', bye)
button3 = tkinter.Button(master=root, text="bye")
button3.pack()
button3['command'] = bye

root.mainloop()
