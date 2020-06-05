from tkinter import *

class Window(Frame):
    def __init__(self, root = None, height = 50, width = 50):
        super().__init__(root)
        self.height = height
        self.width = width
        self.basecolor = "#041129"
        self.drawImage()
        
    def drawImage(self):
        self.rowW = self.height
        self.rowH = self.width / 10
        
        # Initialize Frames
        topFrame = Frame(self,width = self.rowW, height = self.rowH * 5)
        middleFrame = Frame(self,width = self.rowW, height = self.rowH * 4)
        bottomFrame = Frame(self,width = self.rowW, height = self.rowH)
        
        # Style Frames
        self.styleTopFrame(topFrame)   
        self.styleMidFrame(middleFrame)   
        self.styleBottomFrame(bottomFrame)        

        # Layout Frames
        topFrame.grid(row = 0, column = 0)
        middleFrame.grid(row = 1, column = 0)
        bottomFrame.grid(row = 2, column = 0)
        
        # Draw self
        self.pack()


    def styleTopFrame(self, parent):
        # Design Top Frame
        tHeight = self.rowH * 5
        tWidth = self.rowW
        tfColor = self.basecolor
        parent.configure(bg = tfColor)
        tcanvas = Canvas(parent, width = tWidth, height = tHeight, bg = tfColor)
        
        # Add Label
        tcanvas.create_text(tWidth / 2, 5, anchor = "n", text ="Top Frame", fill = "white") # For some reason using label destroys the layout
        
        ## Configure Circle 1
        c1Width = 10 + tHeight / 2 
        c1Height = 10 + tHeight / 2
        c1TopX = 60
        c1TopY = (tHeight / 2) - (c1Height / 2)
        tcanvas.create_oval(c1TopX, c1TopY , c1TopX + c1Width, c1TopY + c1Height, fill = "white", outline="")
        tcanvas.pack()
        
        ## Configure Circle 2
        c2Width = c1Width / 1.23
        c2Height = c1Height / 1.23
        c2TopX = c1TopX
        c2TopY = c1TopY
        tcanvas.create_oval(c2TopX, c2TopY , c2TopX + c2Width, c2TopY + c2Height, fill = tfColor, outline="")
        
        ## Configure Star
        csWidth = c2Width * .9
        csHeight = c2Height * .9
        csTopX = c2TopX + (c2Width / 2) - 30
        csTopY = c2TopY + (c2Height / 2) - 30
        self.createStar(tcanvas, csTopX, csTopY, 28, 7, outline = None, width = .8)
    

    def styleMidFrame(self, parent):
        fHeight = self.rowH * 4
        fWidth = self.rowW
        frameColor = "light blue"
        parent.configure(bg = frameColor)
        
        # Setup Left Column
        lcHeight = fHeight
        lcWidth = fWidth * (2/5)
        leftColor = "white"
        leftCol = Frame(parent, bg = leftColor, width = lcWidth, height = lcHeight)
        leftCol.grid(row = 0, column = 0, columnspan = 1)
        
        lcanvas = Canvas(leftCol, width = lcWidth, height = lcHeight, bg = "white")
        lcanvas.pack(fill = BOTH)
        
        ## Add Label
        lcanvas.create_text(5, 5, anchor = "nw", text = "First Frame")
        
        ## Create Star
        sTopX = lcWidth / 2
        sTopy = lcHeight / 2
        self.createStar(lcanvas, sTopX, sTopy, 50, 15, outline = "light gray", width = 1)
        
        
       
        # Setup Right Column
        rcHeight = fHeight
        rcWidth = fWidth * (3/5)
        rightCol = Frame(parent, width = rcWidth, height = rcHeight)
        rightCol.grid(row = 0, column = 1, columnspan = 2)
        
        ## Top Row
        rtWidth = rcWidth
        rtHeight = rcHeight / 2
        rtColor = "blue"
        rtop = Frame(rightCol, width = rtWidth, height = rtHeight, bg = rtColor)
        rtop.grid(row = 0, column = 0)
        
        ### Add Label
        rtlabel = Label(rtop, text = "Frame Two", bg = "blue", fg = "white")
        rtop.pack_propagate(False)
        rtlabel.pack(side=TOP, anchor=NW)
        
        ## Bottom Row
        rbWidth = rcWidth
        rbHeight = rcHeight / 2
        rbColor = "red"
        rbot = Frame(rightCol, width = rbWidth, height = rbHeight, bg = rbColor)
        rbot.grid(row = 1, column = 0, columnspan = 2)
        
        ### Add Label
        rblabel = Label(rbot, text = "Frame Three", bg = "red", fg = "white")
        rbot.pack_propagate(False)
        rblabel.pack(side=TOP, anchor=NW)
    
    
    def styleBottomFrame(self, parent):
        parent.configure(bg = self.basecolor)
        
        # Setup Left Column
        lWidth = self.rowW / 2
        lHeight = self.rowH
        lframe = Frame(parent, width = lWidth, height = lHeight, bg = self.basecolor)
        lframe.grid(row = 0, column = 0)
        
        ## Add Label
        rblabel = Label(lframe, text = "Bottom Frame", bg = self.basecolor, fg = "white")
        lframe.pack_propagate(False)
        rblabel.pack(side = TOP, anchor = NW)
        
        # Setup Right Column
        rWidth = self.rowW / 2
        rHeight = self.rowH
        rframe = Frame(parent, width = rWidth, height = rHeight, bg = self.basecolor)
        rframe.grid(row = 0, column = 1)
        
        ## Add Label
        rlabel = Label(rframe, text = "Job J Lipat", bg = self.basecolor, fg = "white")
        rframe.pack_propagate(False)
        rlabel.pack(side = LEFT)
        

    def createStar(self, canvas, x,y,p,t, outline= "#476042", fill='yellow', width = 1):
        points = []
        for i in (1,-1):
            points.extend((x, y + i*p))
            points.extend((x + i*t, y + i*t))
            points.extend((x + i*p, y))
            points.extend((x + i*t, y - i * t))

        canvas.create_polygon(points, outline=outline, 
                                fill=fill, width=width)
        
        
        
tk = Tk()
tk.geometry("600x700")
tk.resizable(False, False)
win = Window(tk, 600, 700)
tk.mainloop()
