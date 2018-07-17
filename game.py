import tkinter as tk
import time
import random
def start(population = "human"):
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.focus_force()

    c = tk.Canvas(master = root, width = 1280, height = 720)
    class player():
        def __init__(self,c,control,color = "black"):
            
            self.x = 200
            self.y = 160
            self.vel = 0
            self.c = c
            self.timer = 0
            self.alive = True
            self.playerimage = self.c.create_rectangle(self.x,self.y,self.x+50,self.y+50,fill = color)
            if control == "human":
                root.bind("w",lambda event:self.jump())

        def gravity(self):
            if self.alive:
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

        def hide(self):
            self.c.delete(self.playerimage)




    class pipe():
        def __init__(self,c,x):
            self.x = x
            self.y = 0
            self.gapstart = random.randint(200,500)
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
                
                

    players = []
    if population == "human":
        play = player(c,"human")
        players.append(play)
        player_fitness = 0
    else:
        for i in population:
            i.play = player(c,"bot",color = i.color)
            players.append(i.play)
            
    pipe1 = pipe(c,700)
    pipe2 = pipe(c,1400)

    pipelist = [pipe1,pipe2]
    playing = True
    c.pack()
    while playing:
        
        for i in players:
            i.gravity()
            
        for i in pipelist:
            i.update()

        #getting input
        pipelist.sort(key=lambda x: x.x, reverse=False)
        if population != "human":
            for i in population:
                if i.play.alive:
                #print(i.calculate_action([[i.play.y/720,(pipelist[0].x -200 )/700,(pipelist[0].y)/720,(pipelist[1].y)/720]]))
                    if i.calculate_action([[i.play.y/720,(pipelist[0].x -200 )/700,(pipelist[0].y)/720,(pipelist[1].y)/720]]) == [1]:
                        i.play.jump()
        #taking action

        for k in players:
            for i in pipelist:
                for j in range(2):
                    if k.alive:
                        if j == 0:
                            if k.intersects(i.x,0,i.gapstart): #top pipe
                                k.alive = False
                                k.hide()
                        elif j == 1:     #bottom pipe
                            if k.intersects(i.x,720 - i.lengthbot,i.lengthbot):
                                k.alive = False
                                k.hide()
            
        for i in players:
            if i.y < 0 or i.y > 720 and i.alive:
                i.alive = False
                i.hide()
        if population != "human":
            for i in population:
                if i.play.alive:
                    i.fitness += 8
        else:
            player_fitness += 8
                

        #if not i.alive:
            #playing = False
        playing = False
        for i in players:
            if i.alive:
                playing = True
        root.update()
        if population == "human":
            time.sleep(0.01666666)




    root.destroy()
    if population == "human":
        print("Fitness of human :",player_fitness)
    else:
        population.sort(key=lambda x: x.fitness, reverse=True)
        table_data = []
        mean_calc = 0
        for i in population:
            table_data.append([i.color_name,i.fitness])
            mean_calc += i.fitness
            """if count > len(colors)-1:
                count = 0
            #print("Fitness of ",i.color,":",i.fitness)
            table_data.append([i.play.color,round(i.fitness,3)])
            mean_calc.append(i.fitness)
            count += 1"""
    


        mean = round(mean_calc/len(population),3)
        return population,table_data,mean


if __name__ == "__main__":
    start()

