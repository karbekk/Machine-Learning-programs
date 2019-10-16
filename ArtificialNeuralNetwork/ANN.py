import numpy as np
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)
#print(X),k
deno = np.amax(X,axis=0)
#print(aa)
X = X/deno
y = y/100
print(X)
print(y)



def sigmoid (x):
    return 1/(1 + np.exp(-x))

def derivatives_sigmoid(x): 
    return x * (1 - x)

iteration = 100	#Setting training iterations
error_rate =0.1 		#Setting learning rate-error rate
inputlayer_neurons = 2 		#number of features in data set
hiddenlayer_neurons = 3 	#number of hidden layers neurons
output_neurons = 1 		#number of neurons at output layer


weight_hidden = np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
#print(weight_hidden)
bias_hidden = np.random.uniform(size=(1,hiddenlayer_neurons))
#print("bias value",bias_hidden)
weight_output = np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
bias_output = np.random.uniform(size=(1,output_neurons))


for i in range(iteration):
    hidden_input=np.dot(X,weight_hidden) # h1 = w1*x1+w2*x2+w3*x3
    hidden_input =hidden_input + bias_hidden
    output_hidden_layer = sigmoid( hidden_input)
    #print(output_hidden_layer)
    actual_output = np.dot(output_hidden_layer,weight_output)+bias_output
    y_output = sigmoid(actual_output)
    #print("predicted output",y_output)
    
    
    #Backpropagation
    EO = y-y_output
    outgrad = derivatives_sigmoid(y_output)
    d_output = EO* outgrad
    EH = d_output.dot(weight_output.T)
    hiddengrad = derivatives_sigmoid(output_hidden_layer)
    d_hiddenlayer = EH * hiddengrad
    
    weight_output += output_hidden_layer.T.dot(d_output) *error_rate 
    weight_hidden += X.T.dot(d_hiddenlayer) *error_rate

print("Input: \n" + str(X)) 
print("Actual Output: \n" + str(y))
print("Predicted Output: \n" ,y_output)
