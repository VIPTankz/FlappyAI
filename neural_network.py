
import matrices
import random

class brain():
    def __init__(self):
        self.weights = [] #this will be a 3d array. Each synapse will be a different array inside this array
        self.nodes = [] #this will also be a 2d array. Each layer will be a different array inside this array
                        # in here the activation for each of the nodes will be stored

    def mutate(self):
        x = random.randint(1,2)
        if x == 1:
            pass
            #mutate weights
        elif x == 2:
            pass
            #mutate nodes
        

    def calculate_action(self,input_matrix):  #this should be a function which returns the resulting matrix after being passed
                            #through one layer.
                
        for i in range(len(self.weights)): #this is equal to the number of hidden layers
            #print("multiplies")
            #print(input_matrix)
            #print(self.weights[i])
            input_matrix = matrices.calc(input_matrix,self.weights[i])

            #print("answer")
            #print(input_matrix)
            for j in range(len(self.nodes[i])):
                self.nodes[i][j].activate(input_matrix[0][j]) #the nodes that run the activation are the output of this
                                                            #of this specific operation. 
        print(input_matrix)

        response = []
        for i in range(len(self.nodes[-1])):
            response.append(self.nodes[-1][i].activate(input_matrix[0][i]))
        return response

    def new_random_brain(self,brain_layout):
        #brain_layout takes an array, ie [4,3,3,3,1]
        #each element is a layer of nodes. The number is that element is the number of nodes in the layer.
        #this INCLUDES the input and output layers
        self.weights = []
        self.nodes = []
        for i in range(len(brain_layout)-1): #each synapse
            temp1 = []
            for j in range(brain_layout[i]): #these are each input
                temp2 = []
                for k in range(brain_layout[i+1]):
                    temp2.append(random.randint(-1000,1000)/1000)
                temp1.append(temp2)
            self.weights.append(temp1)
        #print(self.weights)


        for i in range(len(brain_layout)-1):
            temp = []
            for j in range(brain_layout[i+1]):
                temp.append(node())
            self.nodes.append(temp)
            
        """for i in range(len(self.nodes)):
            #print("new layer")
            for j in self.nodes[i]:
                print(j.activation)"""
                                            
class node():
    def __init__(self):
        self.activation = random.randint(-1000,1000)/1000
        
    def activate(self,_input):
        if _input > self.activation:
            return 1
        return 0


if __name__ == "main":
    trial = brain()
    trial.new_random_brain([4,3,3,1])

    print(trial.calculate_action([[2,3,4,5]]))




    
