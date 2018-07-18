import tkinter as tk
import game
import random
import neural_network
import table_scroll
root = tk.Tk()
root.attributes("-fullscreen", True)
c = tk.Canvas(master = root, width = 1280, height = 720)


with open('names.txt', 'r') as f:
    namelist = [line.strip() for line in f]
    
class menu(tk.Frame):
    def __init__(self,main):
        tk.Frame.__init__(self,main,bg="thistle1")

        photo = tk.PhotoImage("")
        
        self.b = tk.Button(self,image = photo,command = lambda root=root:self.leave(root),bg = "red",height = 50,width = 50,
        activebackground = "firebrick3",font=("Helvetica", 15),text="X",compound= tk.CENTER)
        ###DONT CALL FUNCTION EVEYR TIME GET A VARIABVEL
        self.b.place(x =root.winfo_screenwidth()-55,y = 0)
        
        self.title = tk.Label(self,text = "FlappyAI v2",bg = "thistle1",font=("Helvetica", 35))
        self.title.place(relx = .44,rely=0.05)
        
        start = tk.Button(self,text = "Play Flappy Bird",bg = "dark violet",font=("Helvetica", 30),
        activebackground = 'dark violet',command = lambda root=root,c=c:game.start())
        start.place(x = 500,y = 225)

        start_sim = tk.Button(self,text = "Create Simulation",bg = "dark violet",font=("Helvetica", 30),
        activebackground = 'dark violet',command = lambda root=root:self.create(root))
        start_sim.place(x = 485,y = 450)
        
        self.pack(expand="yes",fill="both")

        root.mainloop()

    def leave(self,root):
        root.destroy()

    def create(self,root):
        self.pack_forget()
        options = Options(root)






class Options(tk.Frame):

    def __init__(self,main):
        tk.Frame.__init__(self,main,bg="thistle1")


        self.Label1 = tk.Label(self,text="Population Size:     (This must be even)",bg = "thistle1",font=("Helvetica", 15))
        self.Label1.place(rely = 0.35,relx= .43)
        
        self.Entry1 = tk.Entry(self,font=("Helvetica", 15))
        self.Entry1.place(rely = 0.4,relx= .43)

        self.title = tk.Label(self,text = "FlappyAI",bg = "thistle1",font=("Helvetica", 35))
        self.title.place(relx = .44,rely=0.05)

        self.Label2 = tk.Label(self,text="Orginal Mutations:",bg = "thistle1",font=("Helvetica", 15))
        self.Label2.place(rely = 0.55,relx= .43)

        self.Entry2 = tk.Entry(self,font=("Helvetica", 15))
        self.Entry2.place(rely = 0.6,relx= .43)

        self.Confirm_Button = tk.Button(self,command = lambda root=root:self.create_generation(root),font=("Helvetica", 15) ,text="Confirm",cursor = "pirate")
        self.Confirm_Button.place(rely = 0.8,relx= .46)

        photo = tk.PhotoImage("")

        self.b = tk.Button(self,  image = photo,command = lambda root=root:self.leave(root),bg = "red",height = 50,width = 50,
        activebackground = 'firebrick3',font=("Helvetica", 15),text="X",compound= tk.CENTER)
        ###DONT CALL FUNCTION EVEYR TIME GET A VARIABVEL
        self.b.place(x =root.winfo_screenwidth()-55,y = 0)

        
        self.pack(expand="yes",fill="both")
        
        root.mainloop()
    def leave(self,root):
        root.destroy()

    def create_generation(self,root):
        x = int(self.Entry1.get())
        y = int(self.Entry2.get())
        self.pack_forget()
        generation = Generations(root,x,y)


class Generations(tk.Frame):

    def __init__(self,main,size,mutation,Generations=0):
        #tk.Frame.__init__(self,main,bg="thistle1")
        self.main = main
        self._max_gen = 0
        population = []
        for i in range(size):
            population.append(neural_network.brain(random.choice(namelist)))
            layout = [4]
            for j in range(random.randint(1,5)):
                layout.append(random.randint(1,10))
            layout.append(1)
                
            population[i].new_random_brain(layout)

        self.generation_screen(population)

    def generation_screen(self,population):
        population,table_data,mean = game.start(population = population)

        #reproduction stuff below
        open_spaces = 0
        for i in population[:int(len(population)/10)]:
            i.lives = 3
        for i in population[int(len(population)/4):]:
            i.lives -= 1
            if i.lives == 0:
                open_spaces += 1
                population.remove(i)
                

        for i in population:
            i.fitness = 0


        #print(open_spaces)
        for i in range(open_spaces):
            #print("created new creature")
            x = random.randint(1,4)
            if x == 1: #adds new creature
                population.append(neural_network.brain(random.choice(namelist)))
                layout = [4]
                for j in range(random.randint(1,5)):
                    layout.append(random.randint(1,10))
                layout.append(1)
                    
                population[-1].new_random_brain(layout)
            else:#duplicate and mutate
                
                x = random.choice(population[:int(len(population)/10)])
                temp = neural_network.brain(x.color_name)
                temp.load_genome(x.weights,x.nodes)
                temp.mutate()
                population.append(temp)
                
        
        tk.Frame.__init__(self,self.main,bg="thistle1")
        photo = tk.PhotoImage("")
        self.b = tk.Button(self,  image = photo,command = lambda root=root:self.leave(root),bg = "red",height = 50,width = 50,
        activebackground = 'firebrick3',font=("Helvetica", 15),text="X",compound= tk.CENTER)
        self.b.place(x =root.winfo_screenwidth()-55,y = 0)
        
        self.title = tk.Label(self,text = "Generation: "+str(self._max_gen),font=("Helvetica", 30),bg = "thistle1")
        self.title.place(rely = 0.05,relx= 0.40)
        self._max_gen += 1

        self.history_button = tk.Button(self,  image = photo,command = lambda root=root:self.leave(root),bg = "dark violet",height = 100,width = 360,
        activebackground = 'dark violet',font=("Helvetica", 25),text="History",compound= tk.CENTER)
        self.history_button.place(x = 270,y = 200)
        
        self.multi_step_button = tk.Button(self,  image = photo,command = lambda:self.generation_screen(population),bg = "dark violet",height = 100,width = 360,
        activebackground = 'dark violet',font=("Helvetica", 25),text="Multi-Step Generation",compound= tk.CENTER)
        self.multi_step_button.place(x = 60,y = 400)
        
        self.quick_generation_button = tk.Button(self,  image = photo,command = lambda root=root:self.advance_generation(c,root,population,main,quick_gen = True),bg = "dark violet",height = 100,width = 360,
        activebackground = 'dark violet',font=("Helvetica", 25),text="Quick Generation",compound= tk.CENTER)
        self.quick_generation_button.place(x = 480,y = 400)
        
        self.auto_generation = tk.Button(self,  image = photo,command = lambda root=root:self.advance_generation_multiple(c,root,population,main,quick_gen = True),bg = "dark violet",height = 100,width = 360,
        activebackground = 'dark violet',font=("Helvetica", 25),text="Auto generation",compound= tk.CENTER)
        self.auto_generation.place(x = 270,y = 560)

        table_data = table_data[:int(len(table_data)/10)] + table_data[int(len(table_data)*9/10):]

        height = ((len(table_data)*34)+44+15)
        if height > 550:
            height = 550
        
        self.Border = tk.Label(self,image = photo,bg="black",width= 300+35,height=height)
        self.Border.place(y=140,x=890)
        
        self.table = table_scroll.Table(root, ["Name", "Fitness"], column_minwidths=[150, 150],height = 500)
        self.table.place(y=150,x=900)
        #array = [[13,13],[123,31]]
        self.table.set_data(table_data)        

        self.mean_label = tk.Label(self,text = "Mean Fitness: "+str(round(mean,2)),font=("Helvetica", 14),image = photo,width = 300,height = 100,compound= tk.CENTER,bg="thistle1")#,bg="thistle1"
        self.mean_label.place(y=20,x=900)     

        self.pack(expand="yes",fill="both")
        
        root.mainloop()

            
            
            
        
    def leave(self,root):
        root.destroy()






menu = menu(root)








