# 2
import tkinter

# 3
window = tkinter.Tk()

# 5 Adding a widget
greeting = tkinter.Label(text = "Hello World")
greeting.pack()

# 8
w = tkinter.Canvas(window, width = 200, height = 200)
w.pack()

canvas_height = 200
canvas_width = 200
y = int(canvas_height/2)

w.create_rectangle(50, 20, 150, 80, fill = "#476042")
w.create_rectangle(65, 35, 135, 65, fill = "yellow")

w.create_line(0, 0, 50, 20, fill = "#476042", width = 3)
w.create_line(0, 100, 50, 80, fill = "#476042", width = 3)
w.create_line(150, 20, 200, 0, fill = "#476042", width = 3)
w.create_line(150, 80, 200, 100, fill = "#476042", width = 3)

w.create_text(y, y, text = "Python")

# 9
frame = tkinter.Frame(window)
frame.pack()

bottomframe = tkinter.Frame(window)
bottomframe.pack(side = tkinter.BOTTOM)

redbutton = tkinter.Button(frame, text = "Red", fg = 'red')
redbutton.pack(side = tkinter.LEFT)

greenbutton = tkinter.Button(frame, text = "Brown", fg = 'brown')
greenbutton.pack(side = tkinter.LEFT)

bluebutton = tkinter.Button(frame, text = "Blue", fg = 'blue')
bluebutton.pack(side = tkinter.LEFT)

blackbutton = tkinter.Button(bottomframe, text = "Black", fg = 'black')
blackbutton.pack(side = tkinter.BOTTOM)


# 7
window.mainloop()
