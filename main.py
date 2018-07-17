import tkinter as tk
import game
import random
import neural_network
root = tk.Tk()
root.attributes("-fullscreen", True)
c = tk.Canvas(master = root, width = 1280, height = 720)
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
        population = []
        for i in range(size):
            population.append(neural_network.brain())
            layout = [4]
            for i in range(random.randint(1,5)):
                population.append(random.randint(1,10))
            population[i].new_random_brain([4,3,3,1])













menu = menu(root)









