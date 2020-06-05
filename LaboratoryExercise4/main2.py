from tkinter import *

class Window(Frame):
    def __init__(self, root = None, height = 50, width = 50):
        super().__init__(root)
        self.height = height
        self.width = width
        self.basecolor = "gray"
        self.drawImage()
        
    def drawImage(self):
        rowW = self.height
        rowH = self.width / 10
        
        topFrame = Frame(self)
        middleFrame = Frame(self)
        bottomFrame = Frame(self)
        


        topFrame.grid(row = 0, column = 0)
        middleFrame.grid(row = 1, column = 0)
        bottomFrame.grid(row = 2, column = 0)
        
        self.pack()


    def styleTopFrame(self, parent, rowW, rowH):
        # Design Top Frame
        tHeight = rowH * 5
        tfColor = self.basecolor
        parent.configure(bg = tfColor)
        tcanvas = Canvas(parent, width = rowW, height = tHeight, bg = tfColor)
        tcanvas.create_text(rowW / 2, 5, anchor = "n", text ="Top Frame")
        
        # Configure Circle 1
        cWidth = 10 + tHeight / 2 
        cHeight = 10 + tHeight / 2
        cTopX = 30
        cTopY = (tHeight / 2) - (cHeight / 2)
        tcanvas.create_oval(cTopX, cTopY , cTopX + cWidth, cTopY + cHeight, fill = "blue", outline="")
        tcanvas.pack()
        
        # Configure Circle 2
        c2Width = cWidth / 1.23
        c2Height = cHeight / 1.23
        c2TopX = cTopX
        c2TopY = cTopY
        tcanvas.create_oval(c2TopX, c2TopY , c2TopX + c2Width, c2TopY + c2Height, fill = tfColor, outline="")
        
        # Configure Star
        csWidth = c2Width * .9
        csHeight = c2Height * .9
        csTopX = c2TopX + (c2Width / 2) - 30
        csTopY = c2TopY + (c2Height / 2) - 30
        self.createStar(tcanvas, csTopX, csTopY, 50, 15, outline = None, width = .9)
    

    def styleMidFrame(self, parent, rowW, rowH):
        fHeight = rowH * 4
        fWidth = rowW
        frameColor = "light blue"
        parent.configure(bg = frameColor)
        
        # Setup Left Column
        lcHeight = fHeight
        lcWidth = fWidth * (2/5)
        leftColor = "white"
        leftCol = Frame(parent, bg = leftColor, width = lcWidth, height = lcHeight)
        
        lcanvas = Canvas(leftCol, width = lcWidth, height = lcHeight, bg = "white")
        lcanvas.pack(fill = BOTH)
        
        lcanvas.create_text(5, 5, anchor = "nw", text = "First Frame")
        
        sTopX = lcWidth / 2
        sTopy = lcHeight / 2
        self.createStar(lcanvas, sTopX, sTopy, 50, 15, outline = "light gray", width = 1)
        
        
       
        # Setup Right Column
        rcHeight = fHeight
        rcWidth = fWidth * (3/5)
        rightCol = Frame(parent, width = rcWidth, height = rcHeight)
        rightCol.rowconfigure(0, weight = 1)
        rightCol.rowconfigure(1, weight = 1)
        
        rtWidth = rcWidth
        rtHeight = rcHeight / 2
        rtColor = "blue"
        rtop = Frame(rightCol, width = rtWidth, height = rtHeight, bg = rtColor)
        rtop.grid(row = 0, column = 0, columnspan = 2)
        
        rtlabel = Label(rtop, text = "Frame Two")
        # rtlabel.pack()
        
        rbWidth = rcWidth
        rbHeight = rcHeight / 2
        rbColor = "red"
        rbot = Frame(rightCol, width = rbWidth, height = rbHeight, bg = rbColor)
        rbot.grid(row = 1, column = 0, columnspan = 2)
        
        leftCol.grid(row = 0, column = 0, columnspan = 1)
        rightCol.grid(row = 0, column = 1, columnspan = 2)
    
    
    def styleBottomFrame(self, parent, rowW, rowH):
        parent.configure(bg = self.basecolor)


    def createStar(self, canvas, x,y,p,t, outline= "#476042", fill='yellow', width = 1):
        points = []
        for i in (1,-1):
            points.extend((x,	      y + i*p))
            points.extend((x + i*t, y + i*t))
            points.extend((x + i*p, y))
            points.extend((x + i*t, y - i * t))

        canvas.create_polygon(points, outline=outline, 
                                fill=fill, width=width)
        
        
        
tk = Tk()
tk.geometry("600x700")
win = Window(tk, 600, 700)
tk.mainloop()
