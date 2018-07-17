import tkinter as tk
import time
import random
def start(control = "human"):
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.focus_force()

    c = tk.Canvas(master = root, width = 1280, height = 720)
    class player():
        def __init__(self,c,control):
            
            self.x = 200
            self.y = 160
            self.vel = 0
            self.c = c
            self.timer = 0
            self.alive = True
            self.playerimage = self.c.create_rectangle(self.x,self.y,self.x+50,self.y+50,fill = "black")
            if control == "human":
                root.bind("w",lambda event:self.jump())

        def gravity(self):
            originaly = self.y
            self.y += 15
            if self.vel > 0:
                self.y -= self.vel/7
                self.vel -= 5
            self.c.move(self.playerimage,0,self.y-originaly)
            if self.timer > 0:
                self.timer -= 1

            

        def jump(self):
            if self.timer == 0:
                self.vel = 180
                self.timer = 12

        def intersects(self, xcord,ycord,length):
            if (self.x + 50 < xcord or self.x > xcord + 50 or self.y > ycord + length or self.y + 50 < ycord):
                return False
            return True



    class pipe():
        def __init__(self,c,x):
            self.x = x
            self.y = 0
            self.gapstart = 200
            self.gap = 200
            self.c = c
            self.lengthbot = 720 - self.gapstart - self.gap
            self.pipetop = self.c.create_rectangle(self.x,self.y,self.x+50,self.gapstart,fill = "black")
            self.pipebottom = self.c.create_rectangle(self.x,self.gapstart + self.gap,self.x+50,720,fill = "black")

            
        def update(self):
            self.x -= 8
            self.c.move(self.pipetop,-8,self.y)
            self.c.move(self.pipebottom,-8,self.y)
            if self.x < -50:
                oldgap = self.gapstart
                self.x = 1350
                self.gapstart = random.randint(200,500)
                self.lengthbot = 720 - self.gapstart - self.gap

                del self.pipetop
                del self.pipebottom
                self.pipetop = self.c.create_rectangle(self.x,self.y,self.x+50,self.gapstart,fill = "black")
                self.pipebottom = self.c.create_rectangle(self.x,self.gapstart + self.gap,self.x+50,720,fill = "black")            
                
                


                
    play = player(c,"human")
    pipe1 = pipe(c,700)
    pipe2 = pipe(c,1400)

    pipelist = [pipe1,pipe2]
    playing = True
    c.pack()
    while playing:
        play.gravity()
        for i in pipelist:
            i.update()

        for i in pipelist:
            for j in range(2):
                if j == 0:
                    if play.intersects(i.x,0,i.gapstart): #top pipe
                        play.alive = False
                elif j == 1:     #bottom pipe
                    if play.intersects(i.x,720 - i.lengthbot,i.lengthbot):
                        play.alive = False
            

        if play.y < 0 or play.y > 720:
            play.alive = False

        if not play.alive:
            playing = False
        root.update()
        time.sleep(0.01666666)

    root.destroy()


if __name__ == "__main__":
    start()


