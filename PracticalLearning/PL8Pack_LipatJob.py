# 2
import tkinter as tk

root = tk.Tk()

"""
w = tk.Label(root, text = "Red Sun", bg = "red", fg = "white")
w.pack()
w = tk.Label(root, text = "Green Grass", bg = "green", fg = "black")
w.pack()
w = tk.Label(root, text = "Blue Sky", bg = "blue", fg = "white")
w.pack()
"""

"""
# 3
w = tk.Label(root, text = "Red Sun", bg = "red", fg = "white")
w.pack(fill = tk.X)
w = tk.Label(root, text = "Green Grass", bg = "green", fg = "black")
w.pack(fill = tk.X)
w = tk.Label(root, text = "Blue Sky", bg = "blue", fg = "white")
w.pack(fill = tk.X)
"""

"""
# padx
w = tk.Label(root, text = "Red Sun", bg = "red", fg = "white")
w.pack(fill = tk.X, padx = 10)
w = tk.Label(root, text = "Green Grass", bg = "green", fg = "black")
w.pack(fill = tk.X, padx = 10)
w = tk.Label(root, text = "Blue Sky", bg = "blue", fg = "white")
w.pack(fill = tk.X, padx = 10)
"""

"""
# pady
w = tk.Label(root, text = "Red Sun", bg = "red", fg = "white")
w.pack(fill = tk.X, pady = 10)
w = tk.Label(root, text = "Green Grass", bg = "green", fg = "black")
w.pack(fill = tk.X, pady = 10)
w = tk.Label(root, text = "Blue Sky", bg = "blue", fg = "white")
w.pack(fill = tk.X, pady = 10)
"""

"""
# ipadx
w = tk.Label(root, text = "Red Sun", bg = "red", fg = "white")
w.pack()
w = tk.Label(root, text = "Green Grass", bg = "green", fg = "black")
w.pack(ipadx = 10)
w = tk.Label(root, text = "Blue Sky", bg = "blue", fg = "white")
w.pack()
"""

"""
# ipady
w = tk.Label(root, text = "Red Sun", bg = "red", fg = "white")
w.pack()
w = tk.Label(root, text = "Green Grass", bg = "green", fg = "black")
w.pack(ipadx = 10)
w = tk.Label(root, text = "Blue Sky", bg = "blue", fg = "white")
w.pack(ipady = 10)
"""

"""
# Left to Right
w = tk.Label(root, text = "red", bg = "red", fg = "white")
w.pack(padx = 5, pady = 10, side = tk.LEFT)
w = tk.Label(root, text = "green", bg = "green", fg = "black")
w.pack(padx = 5, pady = 20, side = tk.LEFT)
w = tk.Label(root, text = "blue", bg = "blue", fg = "white")
w.pack(padx = 5, pady = 20, side = tk.LEFT)
"""

# Right to Left
w = tk.Label(root, text = "red", bg = "red", fg = "white")
w.pack(padx = 5, pady = 10, side = tk.RIGHT)
w = tk.Label(root, text = "green", bg = "green", fg = "black")
w.pack(padx = 5, pady = 20, side = tk.RIGHT)
w = tk.Label(root, text = "blue", bg = "blue", fg = "white")
w.pack(padx = 5, pady = 20, side = tk.RIGHT)


tk.mainloop()