import tkinter as tk
import time
import random
import table_scroll


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
        
        self.title = tk.Label(self,text = "FlappyAI",bg = "thistle1",font=("Helvetica", 35))
        self.title.place(relx = .44,rely=0.05)
        
        start = tk.Button(self,text = "Play Flappy Bird",bg = "dark violet",font=("Helvetica", 30),
        activebackground = 'dark violet',command = lambda root=root,c=c: self.playgame(root,c))
        start.place(x = 500,y = 225)

        start_sim = tk.Button(self,text = "Create Simulation",bg = "dark violet",font=("Helvetica", 30),
        activebackground = 'dark violet',command = lambda root=root:self.create(root))
        start_sim.place(x = 485,y = 450)
        
        self.pack(expand="yes",fill="both")
        
    def leave(self,root):
        root.destroy()

    def playgame(self,root,c):
        self.pack_forget()
        playgame(root,c,0,0)

    def create(self,root):
        self.pack_forget()
        options = Options(root)
        
###IN THE FUTURE MAKE A CONTROOLER CLASS TO INSTANTISE AND MANAGE ALL MENU FRAMES PLEASE
class Options(tk.Frame):

    def __init__(self,main):
        tk.Frame.__init__(self,main,bg="thistle1")


        self.Label1 = tk.Label(self,text="Population Size:",bg = "thistle1",font=("Helvetica", 15))
        self.Label1.place(rely = 0.35,relx= .43)
        
        self.Entry1 = tk.Entry(self,font=("Helvetica", 15))
        self.Entry1.place(rely = 0.4,relx= .43)

        self.title = tk.Label(self,text = "FlappyAI",bg = "thistle1",font=("Helvetica", 35))
        self.title.place(relx = .44,rely=0.05)

        self.Label2 = tk.Label(self,text="Orginal Mutations:",bg = "thistle1",font=("Helvetica", 15))
        self.Label2.place(rely = 0.55,relx= .43)

        self.Entry2 = tk.Entry(self,font=("Helvetica", 15))
        self.Entry2.place(rely = 0.6,relx= .43)

        self.Confirm_Button = tk.Button(self,command = lambda root=root:self.stuff(root),font=("Helvetica", 15) ,text="Confirm",cursor = "pirate")
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

    def stuff(self,root):
        x = int(self.Entry1.get())
        y = int(self.Entry2.get())
        self.pack_forget()
        generation = Generations(root,x,y)
        

class Generations(tk.Frame):

    def __init__(self,main,size,mutation,Generations=0):
        tk.Frame.__init__(self,main,bg="thistle1")

        photo = tk.PhotoImage("")

        self.b = tk.Button(self,  image = photo,command = lambda root=root:self.leave(root),bg = "red",height = 50,width = 50,
        activebackground = 'firebrick3',font=("Helvetica", 15),text="X",compound= tk.CENTER)
        ###DONT CALL FUNCTION EVEYR TIME GET A VARIABVEL
        self.b.place(x =root.winfo_screenwidth()-55,y = 0)


        
        self._max_gen = Generations
        self.Label1 = tk.Label(self,text = "Generation: "+str(self._max_gen),font=("Helvetica", 30),bg = "thistle1")
        self.Label1.place(rely = 0.05,relx= 0.40)

        table_data = playgame(root,c,size,mutation)
        

        ####
        height = ((len(table_data)*39.25)+20)
        if height > 550:
            height = 550
        print(height)
        self.Boarder = tk.Label(self,image = photo,bg="black",width= 300+35,height=height)
        self.Boarder.place(y=140,x=940)
        
        table = table_scroll.Table(root, ["Name", "Fitness"], column_minwidths=[150, 150],height = 500)
        table.place(y=150,x=950)
        #array = [[13,13],[123,31]]
        table.set_data(table_data)

        



        ####
        self.pack(expand="yes",fill="both")
        root.mainloop()
        
    def leave(self,root):
        root.destroy()        
menu = menu(root)
#menu.place()
root.update()

GEN = []

"""
for i in GEN:
    for j in GEN[i]:
        square = i.color
        name = i.color
        fitness = i.fitness
view = Number
"""

class brain():
    def __init__(self,c):
        self.nodes = []
        self.axons = []
        self.fitness = 0
        self.axon_num = 9
        self.node_num = 6
        self.play = player(c)

    ##################### tyler - increases the fitness every frame when the game runs
    def update_fitness(self):
        if self.play.alive:
            self.fitness += 8

    def set_random_values(self):
        self.add_node("input",1)
        self.add_node("input",2)
        self.add_node("input",3)
        self.add_node("input",4)
        self.add_node("output",5,_action = "jump")
        ######
        self.add_node("input",6)
        self.add_node("input",7)
        self.add_node("input",8)
        
        self.add_axon(1,6,(random.randint(-100,100)/100),True,5) #checking for loop
        self.add_axon(6,7,(random.randint(-100,100)/100),True,6)
        self.add_axon(7,5,(random.randint(-100,100)/100),True,7)
        self.add_axon(7,8,(random.randint(-100,100)/100),True,8)
        ######
        self.add_axon(1,5,(random.randint(-100,100)/100),True,1) #_in,_out,_weight,_status,_id 
        self.add_axon(2,5,(random.randint(-100,100)/100),True,2)
        self.add_axon(3,5,(random.randint(-100,100)/100),True,3)
        self.add_axon(4,5,(random.randint(-100,100)/100),True,4) #the idea here has nothing to do with node id, just used to track axons

    def mutate(self,show):
        x = random.randint(1,5)
        if x == 1:
            if show:
                print("Change weight")
            self.mutate_weight()
        if x == 2:
            if show:
                print("enable node")
            self.mutate_enable()
        if x == 3:
            if show:
                print("disable node")
            self.mutate_disable()
        if x == 4:
            if show:
                print("Add axon")
            self.mutate_add_axon(show)
        if x == 5:
            if show:
                print("add node")
            self.mutate_add_node(show)

    def mutate_disable(self):

        choices = []
        for i in self.axons:
            if i._status:
                choices.append(i)

        random.shuffle(choices)
        if len(choices) > 0:
            choices[0]._status = False
        else:
            self.mutate_enable()

    def mutate_enable(self):
        choices = []
        for i in self.axons:
            if not i._status:
                choices.append(i)

        random.shuffle(choices)
        if len(choices) > 0:
            choices[0]._status = False
        else:
            self.mutate_disable()       

    def mutate_weight(self):
        x = random.randint(0,len(self.axons)-1)
        self.axons[x]._weight += random.randint(-100,100)/100

    def mutate_add_axon(self,show):

        _in_choices = self.nodes[:]
        _in_choices.remove(_in_choices[4])
        #_in_choices = self.nodes.remove(self.nodes[4])

        _out_choices = self.nodes[4:]
        #for i in _out_choices:
            #print(i._id)

        random.shuffle(_in_choices)
        random.shuffle(_out_choices)

        _in = None
        weight = random.randint(-100,100)/100
        done = False
        for i in _in_choices:
            for j in _out_choices:
                #print(i._id,j._id)
                self.add_axon(i._id,j._id,weight,True,self.axon_num)
                if i._id != j._id and self.check_all_parents(i._id):
                    ok = True
                    for k in self.axons:
                        if k._in == i._id and j._id == k._out:
                            ok = False
                    if ok:
                        _in = i._id
                        _out = j._id
                        done = True
                        break
                else:
                    del self.axons[-1]
            if done:
                break
                    
        if _in != None:
            weight = random.randint(-100,100)/100
            self.add_axon(_in,_out,weight,True,self.axon_num)
            if show:
                print("Added axon with nodes",i._id,"to",j._id)
            self.axon_num += 1
            
        else:
            self.mutate_weight()
            """ for k in self.nodes:
            print("Node:",k._id)
            for p in self.axons:
                print("Axon:")
                print("in:",p._in)
                print("out:",p._out)  """         

    ################################## tyler - adding add node
    def mutate_add_node(self,show):
        self.add_node("hidden",self.node_num) #creates a new node#
        if show:
            print("Node",self.node_num,"added")
        c = self.node_num
        _before_choices = self.nodes[:]
        _before_choices.remove(_before_choices[4]) #creates a list with everything except the output as this cannot be before a node
        _before_choices.pop()

        weight = random.randint(-100,100)/100
        temp_choice = random.choice(_before_choices)
        
        self.add_axon(temp_choice._id,self.node_num,weight,True,self.axon_num) #adds the axon to the node
        if show:
            print("(axon before new nodes) Added axon with nodes",temp_choice._id,"to",self.node_num)
        self.axon_num += 1

        ###    this will check potential other nodes the node can go to

        _out_choices = self.nodes[4:]

        random.shuffle(_out_choices)
        weight = random.randint(-100,100)/100
        for j in _out_choices:
            self.add_axon(self.node_num,j._id,weight,True,self.axon_num)
            """for k in self.nodes:
                print("Node:",k._id)
            for p in self.axons:
                print("Axon:")
                print("in:",p._in)
                print("out:",p._out)"""
            
            if self.node_num != j._id:# and self.check_all_parents(self.node_num):
                check =True
                for i in self.nodes:
                    q =self.check_all_parents(i._id)
                    if not q:
                        check = False
                if check:
                    if show:
                        print("(axon after new nodes) Added axon with nodes",self.node_num,"to",j._id)
                    break
                else:
                    del self.axons[-1]
                    self.axons.pop()
                    
            else:
                #for i in self.axons:
                    #print(i._id)
                del self.axons[-1]
                #self.axons.pop()
                #print("This axon was killed")
                #for i in self.axons:
                    #print(i._id)


        self.axon_num += 1
        self.node_num += 1 

        ###
        
              #this means next time the id will be one higher

    #################################
    def check_all_parents(self,_in):
        for i in self.nodes:
            if _in == i._id:
                x = i.calculate_total_parent_nodes(self.axons,self.nodes,_in,[])
                if x != None:
                    #print("True")
                    return True
                #print("False")
                return False
                
                    
        
    def add_node(self,_type,_id,_action = None):
        self.nodes.append(node(_type,_id,_action))

    def add_axon(self,_in,_out,_weight,_status,_id):
        self.axons.append(axon(_in,_out,_weight,_status,_id))

    def get_inputs(self,bird_y,distance_to_pipe,top_pipe,bottom_pipe):
        for i in self.nodes:
            if i._type == "input":
                if i._id == 1:
                    i._value = bird_y
                elif i._id == 2:
                    i._value = distance_to_pipe
                elif i._id == 3:
                    i._value = top_pipe
                elif i._id == 4:
                    i._value = bottom_pipe
                i._evaluated = True
                




    def calculate_jump(self):

        value = self.calculate_node_value(5)
                
        #print("output",value)

        
        return self.activation(value)

    def calculate_node_value(self,_id):
        val = 0
        for i in self.nodes:
            if i._id == _id: #this finds the correct node
                for j in i._child_nodes:
                    for c in self.nodes:
                        if c._id == j: #this finds the child node
                            
                            if c._evaluated:
                                #print("Parent",i._id,"child",c._id,"evaluated")
                                add = c._value * self.find_axon(c._id , _id) #input, then output
                                val += add
                                #print(add)

                            else:
                                #print("Parent",i._id,"child",c._id,"not evaluated")
                                add = self.calculate_node_value(c._id) * self.find_axon(c._id , _id)
                                val += add
                                #print(add)
                        
                        c._evaluated = True
        
        return val
                        
                                    
    def find_axon(self,_in,_out):
        for i in self.axons:
            if i._in == _in and i._out == _out and i._status:
                return i._weight
        return 0

                
                        
    def activation(self,_input):
        if _input > .5:
            return 1
        return 0
    
    def calculate_children(self):
        for i in self.nodes:
            i.calculate_child_nodes(self.axons)
            
      
                


class node():
    def __init__(self,_type,_id,_action):
        self._type = _type #input, hidden or output 
        self._id = _id #should be incremental
        self._value = 0
        self._action = _action
        
        self._child_nodes = []
        self._total_parent_nodes = []
        self._evaluated = False
        

    def calculate_child_nodes(self,axons):
        for i in axons:
            if i._out == self._id:
                self._child_nodes.append(i._in)
        #print("Parent,",self._id)
        #print("Children",self._child_nodes)
                
    def calculate_parent_nodes(self,axons):
        _parent_nodes = []
        for i in axons:
            if i._in == self._id:
                _parent_nodes.append(i._out)
                                
        return _parent_nodes
################################################################# Reece - Changing the calculation for checking recursion
    #its magic don't touch
    def calculate_total_parent_nodes(self,axons,nodes,start,logs):
        #print(self._id)    
        templog = [logs[:]]
        if self._id in logs:
            #print("hoi")
            return None
        self._total_parent_nodes = []
        x = self.calculate_parent_nodes(axons)
        for i in x:
            self._total_parent_nodes.append(i)
        for i in self._total_parent_nodes:
            templog.append(logs[:])
        #print(templog)            
        temp = x
        count = 0
        for i in temp:
            for j in nodes:
                if j._id == i: #j is the parents which we look for the node with corresponding number
                    templog[count].append(self._id)
                    #print(templog[count])
                    something = j.calculate_total_parent_nodes(axons,nodes,start,templog[count])
                    templog[count].append(something)
                    if something != None:
                        for k in something:
                            if k not in self._total_parent_nodes:
                                self._total_parent_nodes.append(k)
                    else:
                        return None
            count += 1                    
        #print(self._total_parent_nodes)
        return self._total_parent_nodes
#################################################################

        
class axon():
    def __init__(self,_in,_out,_weight,_status,_id):
        self._in = _in #the node that signal is taken from
        self._out = _out #the node that the signal is sent to
        self._weight = _weight #the weight
        self._status = _status #true or false whether axon is active
        self._id = _id #unique id marker


class player():
    def __init__(self,c,control = "bot"):
        self.y = 300
        self.x = 100
        self.vel = 0
        self.acc = 0
        self.c = c
        self.playerimage = self.c.create_rectangle(self.x,self.y,self.x+50,self.y+50,fill = "black") #4 corners
        self.alive = True
        self.dead = False
        self.control = control


        if self.control == "human":
            root.bind("w",lambda event:self.jump())
            self.fitness = 0

        self.cooldown = 0

    ################# tyler - allows the color of the bird to change
    def color_change(self,canvas,color):
        canvas.itemconfig(self.playerimage, fill=color)
        self.color = color
        #print(self.color)
    ###############

        
    def update(self):
        if self.alive:
            if self.control == "human":
                self.fitness += 8
            self.c.move(self.playerimage,-self.x,-self.y)
            self.y += (self.vel + self.acc * 0.5)

            #if self.vel < -2 or self.acc > 0:
            self.vel -= self.acc

            if self.vel > 15:
                self.vel = 15
            self.c.move(self.playerimage,self.x,self.y)
            
            #gravity
            if self.acc > -1.5:
                self.acc -= 0.05
                
            if self.cooldown != 0:
                self.cooldown -= 1

        else:
            if not self.dead:
                self.c.move(self.playerimage,-200,0)
            
            
    def jump(self):
        if self.cooldown == 0:
            self.acc = .8
            #if self.vel < 1:
            self.vel = 0
            self.cooldown = 6

    def check(self,pipelist):
        if self.y > 720 or self.y < 0:
            return False

        for i in pipelist:  
            if self.x + 49 > i.x and self.x+ 49 < i.x + 50 and (self.y < i.gapstart or self.y > i.gapstart + i.gap):
                return False

        return True
        

class pipe():
    def __init__(self,x,randomness = True):
        self.y = 300
        self.x = x
        self.gap = 200
        self.randomness = randomness
        if self.randomness:
            self.gapstart = random.randint(100,500)
        else:
            self.gapstart = 300

            
        self.pipeimage = c.create_rectangle(self.x,0,self.x+50,self.gapstart,fill = "black") #4 corners
        print("REST")
        self.pipeimage2 = c.create_rectangle(self.x,self.gapstart+self.gap,self.x+50,self.gapstart+self.gap+ 700,fill = "black")
    def update(self):
        c.move(self.pipeimage,-self.x,-self.y)
        c.move(self.pipeimage2,-self.x,-self.y)
        self.x -= 8
        #if brain.alive:
            #brain.fitness += 1
        c.move(self.pipeimage,self.x,self.y)
        c.move(self.pipeimage2,self.x,self.y)

        if self.x < -50:
            c.move(self.pipeimage,-self.x,-self.y)
            c.move(self.pipeimage2,-self.x,-self.y)
            self.x = 1300
            c.move(self.pipeimage,self.x,self.y)
            c.move(self.pipeimage2,self.x,self.y)
            if self.randomness:
                self.gapstart = random.randint(100,500)
            self.pipeimage = c.create_rectangle(self.x,0,self.x+50,self.gapstart,fill = "black")
            self.pipeimage2 = c.create_rectangle(self.x,self.gapstart+self.gap,self.x+50,self.gapstart+self.gap+ 700,fill = "black")

        



someweight1 = 0.4
someweight2 = -0.6
someweight3 = 0.7
someweight4 = -0.2
someweight5 = -0.9
someweight6 = 0.3#0.6

######################################################## normal stuff

#brain1 = brain()
"""#brain1.set_random_values()

#brain1.add_node("input",1)
#brain1.add_node("input",2)
brain1.add_node("input",3)
#brain1.add_node("input",4)
brain1.add_node("output",5,_action = "jump")

brain1.add_node("hidden",6)
brain1.add_node("hidden",7)
brain1.add_node("hidden",8)
#####################

brain1.add_node("hidden",9)


brain1.add_axon(3,7,someweight1,True,1)       #this is the broken network for testing

brain1.add_axon(7,8,someweight1,True,2)
brain1.add_axon(8,9,someweight1,True,3)
brain1.add_axon(9,7,someweight1,True,4)

brain1.add_axon(7,5,someweight1,True,5)

population = []
for i in brain1.axons:
    print("in: ",i._in,end ="")
    print(" out: ",i._out)
print(brain1.check_all_parents(3))
"""
#################### - Reece testing dual connection of nodes
"""brain1.add_node("input",3)
brain1.add_node("hidden",4)
brain1.add_node("hidden",5)
brain1.add_node("hidden",6)
brain1.add_node("output",7,_action = "jump")
brain1.add_node("hidden",8)
brain1.add_axon(3,4,someweight1,True,1)
brain1.add_axon(4,5,someweight1,True,2)
brain1.add_axon(4,6,someweight1,True,3)
brain1.add_axon(5,7,someweight1,True,4)
brain1.add_axon(6,7,someweight1,True,5)
brain1.add_axon(6,8,someweight1,True,6)
population = []
for i in brain1.axons:
    print("in: ",i._in,end ="")
    print(" out: ",i._out)
count = 3
for i in brain1.nodes:
    print("Start from:", count)
    print(brain1.check_all_parents(count))
    count += 1
####################
"""
#I am moving the axons and nodes that must be there to the init
"""
brain1.add_axon(1,5,someweight1,True,1) #_in,_out,_weight,_status,_id 
brain1.add_axon(2,5,someweight2,True,2)
brain1.add_axon(3,5,someweight3,True,3)
brain1.add_axon(4,5,someweight4,True,4) #the id (the last one) here has nothing to do with node id, just used to track axons
"""

#brain1.add_axon(1,6,someweight5,True,5)
#brain1.add_axon(6,5,someweight6,True,6)

#brain1.add_axon(2,7,someweight5,True,7)
#brain1.add_axon(7,6,someweight6,True,8)

#brain1.mutate_add_node()
#brain1.calculate_children()
############################################# This is another broken network
"""
brain1 = brain()

brain1.add_node("input",1)
brain1.add_node("input",2)
brain1.add_node("input",3)
brain1.add_node("input",4)
brain1.add_node("output",5,_action = "jump")

brain1.add_node("hidden",6)
brain1.add_node("hidden",7)
brain1.add_node("hidden",8)


brain1.add_axon(1,5,someweight6,True,6)
brain1.add_axon(2,5,someweight5,True,7)
brain1.add_axon(3,5,someweight6,True,8)
brain1.add_axon(4,5,someweight6,True,8)


brain1.add_axon(1,7,someweight5,True,5)
brain1.add_axon(7,6,someweight6,True,6)

brain1.add_axon(6,5,someweight5,True,7)
brain1.add_axon(6,8,someweight6,True,8)
brain1.add_axon(8,7,someweight6,True,8)


brain1.check_all_parents(1)
"""
#############################################

############ tyler
colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

random.shuffle(colors)

############################## Adding the first window of gui






##start_sim = tk.Button(root_menu,text = "Create Simulation",bg = "dark violet",font=("Helvetica", 30),activebackground = 'dark violet')
##start_sim.place(x = 490,y = 450)
##root_menu = tk.Tk()
##root_menu.attributes("-topmost", 1)
##root_menu.focus_force()
##root_menu.attributes("-fullscreen", True)
##root_menu.configure(background='thistle1')
##b = tk.Button(root_menu, text="X", command=leave,bg = "red",height = 4,width = 8,font=("Helvetica", 15),activebackground = 'firebrick3')
##b.place(x = 1190,y = 0)
##title = tk.Label(root_menu,text = "FlappyAI",bg = "thistle1",font=("Helvetica", 35))
##title.place(x = 550,y = 30)

##start = tk.Button(root_menu,text = "Play Flappy Bird",bg = "dark violet",font=("Helvetica", 30),activebackground = 'dark violet',command = lambda c=c: playgame(c))
##start.place(x = 500,y = 225)
##
##start_sim = tk.Button(root_menu,text = "Create Simulation",bg = "dark violet",font=("Helvetica", 30),activebackground = 'dark violet')
##start_sim.place(x = 490,y = 450)



##################################################
def create_population(size,mutation,colors,c):
    pop = [] #creates a list of instances to make up a list

    count = 0

    for i in range(size):
        if count > len(colors)-1:
            count = 0
        #print(colors[count],count)
        pop.append(brain(c))
        pop[i].set_random_values()
        pop[i].play.color_change(c,colors[count])  #canvas, color

        for j in range(mutation):
            pop[i].mutate(False)

        pop[i].calculate_children()
        count += 1
        
    GEN.append(pop)
    return pop


######################

#brain1 = brain()
#brain1.set_random_values()



def playgame(root,c,size,mutation):
    #root = tk.Tk()
    root = root
    play = player(c,control = "human")
    game = True
    #root.attributes("-fullscreen", True)
    #root.focus_force()
    #root.wm_attributes("-topmost", 1)
    
    c.pack()        
    #play = player(control = "human")
    pipes = pipe(800,randomness = False)
    pipes2 = pipe(1400,randomness = False)



    pipelist = [pipes,pipes2]
    start = time.time()
    clock_background = c.create_rectangle(1100,30,1250,80,fill = "grey")
    #playerimage = c.create_rectangle(play.x,play.y,play.x+50,play.y+50,fill = "black") #4 corners
    clock = c.create_text(1170,50,fill="black",font="Times 30 bold",text="Hi")
    #root.attributes("-fullscreen", True)
    print("Playgame")
    population = create_population(size,mutation,colors,c)
    
    while game: 
        root.update()
        for i in population:
            i.play.update()
            
        play.update() #original stuff
        #######################
        xvals = []
        for i in pipelist:
            xvals.append(i.x)

            
        closest_pipe = min(xvals)
        for i in pipelist:
            if i.x == closest_pipe:
                top_pipe = i.gapstart
                bottom_pipe = i.gapstart + i.gap

        for i in population:
            i.get_inputs(i.play.y,( closest_pipe - i.play.x)/10,top_pipe/100,bottom_pipe/100)
            
        #brain1.get_inputs(play.y/100,( closest_pipe - play.x)/10,top_pipe/100,bottom_pipe/100) #origianl stuff
        for i in population:
            jump1 = i.calculate_jump()
            if jump1:
                #print("Jump")
                i.play.jump()
            else:
                #print("No jump")
                pass
        #############################
        end = time.time()
        c.itemconfig(clock, text=str(round(end - start,2)))
        """for i in pipelist:
            for j in population:
                i.update(j)"""

        for i in pipelist:
            i.update()

        for i in population:
            i.update_fitness()

        person_still_going = False
        for i in population:
            if i.play.alive:
                i.play.alive = i.play.check(pipelist)
                survived = i.play.alive
                if survived == True:
                    person_still_going = True

        play.alive = play.check(pipelist)

        if not person_still_going:
            if not play.alive: 
                game = False
        time.sleep(0.01666666666)
      
    #root.mainloop()
    count = 0
    population.sort(key=lambda x: x.fitness, reverse=False)
    table_data = []
    for i in population:
        if count > len(colors)-1:
            count = 0
        #print("Fitness of ",i.color,":",i.fitness)
        table_data.append([i.play.color,i.fitness])
        count += 1
    print("Fitness of human :",play.fitness)
    c.destroy()
    return table_data









    
