from turtle import *

class Disk():
    def __init__(self, name, x, y, height, width):
        self.name = name
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def showdisk(self):
        pu()
        goto(self.x, self.y)
        pd()
        fillcolor("red")
        begin_fill()
        fd(self.width / 2)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width / 2)
        end_fill()

    def newpos(self, x, y):
        self.cleardisk()
        self.x = x
        self.y = y
        self.showdisk()

    def cleardisk(self):
        pu()
        goto(self.x, self.y)
        pd()
        pencolor("white")
        fillcolor("white")
        begin_fill()
        fd(self.width / 2)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width / 2)
        end_fill()

class Pole:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.stack = []
        self.top_position = 0
        self.thickness = 30
        self.length = 210

    def showpole(self):
        speed(0)
        pu()
        color("black")
        goto(self.x, self.y)
        seth(0)
        pd()
        begin_fill()
        fd(self.thickness / 2)
        lt(90)
        fd(self.length)
        lt(90)
        fd(self.thickness)
        lt(90)
        fd(self.length)
        lt(90)
        fd(self.thickness / 2)
        end_fill()

    def pushdisk(self, disk):
        self.stack.append(disk)
        disk.newpos(self.x, self.y + disk.height * len(self.stack))

    def popdisk(self):
        disk = self.stack.pop(len(self.stack) - 1)
        disk.newpos(self.x, self.length + 50)
        return disk