from tkinter import *
from random import choice as ch, randrange as rnd
from PIL import Image
from PIL import ImageTk



root = Tk()
root.geometry('1200x1000')

canv = Canvas(root, bg='#848484')
canv.pack(fill=BOTH, expand=1)
e = Entry(root, width=20)
b = Button(root, text="Score", bg='#848484', fg='#2E2EFE')
l = Label(root, bg='#848484', fg='#FFFFFF', width=2000)


colors = ['#DF0101', '#00FFFF', '#FE2EF7', '#190710', '#2E2EFE', '#F7FE2E']

score = 0
n = 1


class Ball():
    def __init__(self):
        self.x = rnd(111, 888)
        self.y = rnd(111, 444)
        self.r = rnd(22, 55)
        self.dx = rnd(-3, 3)
        self.dy = rnd(-3, 3)
        self.ball = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        self.color = ch(colors)
        canv.itemconfig(self.ball, fill="#610B4B")
        canv.addtag_withtag("ball", self.ball)


    def ricochet_ball(self):
        if self.y <= self.r or self.y + self.r >= 1000:
            self.dy = -self.dy
        if self.x <= self.r or self.x + self.r >= 1200:
            self.dx = -self.dx


    def move_ball(self):
        self.x += self.dx
        self.y += self.dy
        canv.move(self.ball, self.dx, self.dy)


    def new_create(self):
        self.x = rnd(111, 888)
        self.y = rnd(111, 444)
        self.r = rnd(22, 55)
        self.dx = rnd(-3, 3)
        self.dy = rnd(-3, 3)
        self.color = ch(colors)
        canv.itemconfig(self.ball, fill=self.color)

class Apple():
    def __init__(self):
        self.x = rnd(111, 888)
        self.y = rnd(111, 444)
        self.r = 20
        self.dx = rnd(-22, 22)
        self.dy = rnd(-22, 22)
        self.apple = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.apple,fill="green")
        canv.addtag_withtag("apple", self.apple)
        self.image()


    def new_apple(self):
        self.x = rnd(111, 888)
        self.y = rnd(111, 444)
        self.r = 20
        self.dx = rnd(-22, 22)
        self.dy = rnd(-22, 22)
        canv.itemconfig(self.apple)
        self.image()


    def ricochet_apple(self):
        if self.y <= self.r or self.y + self.r >= 1000:
            self.dy = -self.dy
        if self.x <= self.r or self.x + self.r >= 1200:
            self.dx = -self.dx


    def move_apple(self):
        self.x += self.dx
        self.y += self.dy
        canv.move(self.apple, self.dx, self.dy)
        self.image()


    def image(self):
        self.img = Image.open("apple.jpg")
        self.appleimg = ImageTk.PhotoImage(self.img)
        canv.create_image(self.x, self.y, image=self.appleimg)





apples = []
balls = []
for i in range(n):
    balls.append(Ball())
for k in range(n):
    apples.append(Apple())


def miss(event):
    for i in range(len(balls)):
        x_old = balls[i].x
        y_old = balls[i].y
        x_aold = apples[i].x
        y_aold = apples[i].y
        balls[i].new_create()
        apples[i].new_apple()
        canv.move(balls[i].ball, balls[i].x - x_old, balls[i].y - y_old)
        canv.move(apples[i].apple, apples[i].x - x_aold, apples[i].y - y_aold)


def hit(event):
    global score
    for i in range(len(balls)):
        x_old = balls[i].x
        y_old = balls[i].y
        x_aold = apples[i].x
        y_aold = apples[i].y
        balls[i].new_create()
        canv.move(balls[i].ball, balls[i].x - x_old, balls[i].y - y_old)
        apples[i].new_apple()
        canv.move(apples[i].apple, apples[i].x - x_aold, apples[i].y - y_aold)
    score += 5
    l['text'] = str(score)


def update():
    for i in range(len(balls)):
        balls[i].ricochet_ball()
        balls[i].move_ball()
        apples[i].ricochet_apple()
        apples[i].move_apple()
        root.after(30, update)


b.pack()
l.pack()
update()
canv.bind('<Button-1>', miss)
canv.tag_bind("ball" or "apple", '<Button-1>', hit )
root.mainloop()
