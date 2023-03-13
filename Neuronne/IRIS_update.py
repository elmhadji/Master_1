import numpy as np
import matplotlib.pylab as plt
import pandas as pd
from sklearn.model_selection import train_test_split

class NeuralNetwork :

    def __init__(self , input_layer = 4 , output_layer = 3 ,hidden_layer_1 = 4 , hidden_layer_2 = 4):
        
        # the number of neurons
        self.input_layer = input_layer
        self.hidden_layer_1 = hidden_layer_1
        self.hidden_layer_2 = hidden_layer_2
        self.output_layer = output_layer

        # the weigth of each layers
        self.weight_1 = np.random.randn(self.input_layer , self.hidden_layer_1) #  shape : 4,4
        self.weight_2 = np.random.randn(self.hidden_layer_1 , self.hidden_layer_2) #  shape : 4,4
        self.weight_3 = np.random.randn(self.hidden_layer_2 , self.output_layer) #  shape : 4,3

        # the biases

        self.bias_1 = np.random.randn(1 , self.hidden_layer_1)
        self.bias_2 = np.random.randn(1 , self.hidden_layer_2)
        self.bias_3 = np.random.randn(1 , self.output_layer)


    def sigmoid(self, S ):
        return 1/(1 + np.exp(-S))
    
    def sigmoid_derivate (self , S):
        return (np.exp(S)/(np.exp(S)+1)**2)

    def RSME (self , y_hat , y):
        return np.sqrt(np.square(np.subtract(y_hat, y)).mean())

    def RSME_derivate(self , y_hat , y):
        N = y.shape[0]
        diff = y_hat - y
        mse = np.mean(diff ** 2)
        rmse = np.sqrt(mse)
        return diff / (rmse * N)
    
    def feedforward (self , inputs):
        # calculate the dot product of each layer with it weitgh

        self.Z1 = np.dot(inputs , self.weight_1) #+ self.bias_1 #  shape : 120,4 /   shape : 1,4
        self.A1 = self.sigmoid(self.Z1) #  shape : 120,4 

        self.Z2 = np.dot(self.A1 , self.weight_2) #+ self.bias_2  #  shape : 120,4
        self.A2 = self.sigmoid(self.Z2) #  shape : 120,4

        self.Z3 = np.dot(self.A2 , self.weight_3) # + self.bias_3#  shape : 120,3
        self.A3 = self.sigmoid(self.Z3) #  shape : 120,3

        return self.A3
    

    def backpropagation(self  , inputs , y_hat, output , learning_rate = 0.01):
        # calculate the gradient and update the weights

        d_E_y_hat = y_hat - output # shape: 120,3
        d_y_hat_Z3 = self.sigmoid_derivate(self.Z3) # shape: 120,3
        d_Z3_W3 = self.A2 # shape: 120,4
        
        dw3 = np.dot(d_Z3_W3.T, d_E_y_hat * d_y_hat_Z3) # shape: 4,3


        d_Z3_A2 = self.weight_3 #  shape : 4,3
        d_A2_Z2 = self.sigmoid_derivate(self.Z2) #  shape : 120,4
        d_Z2_W2 = self.A1 #  shape : 120,4
        dw2 = np.dot(d_Z2_W2.T , np.dot(d_E_y_hat * d_y_hat_Z3 , d_Z3_A2.T) * d_A2_Z2)  # shape: 4,4

        d_Z2_A1 = self.weight_2 #  shape : 4,4
        d_A1_Z1 = self.sigmoid_derivate(self.Z1) #  shape : 120,4
        d_Z1_W1 =  inputs #  shape : 120,4
        dw1 = np.dot(d_Z1_W1.T , np.dot( np.dot(d_E_y_hat * d_y_hat_Z3 , d_Z3_A2.T) * d_A2_Z2  ,d_Z2_A1.T )* d_A1_Z1 )  # shape: 4,4

        
        self.weight_1 -= learning_rate * dw1
        self.weight_2 -= learning_rate * dw2
        self.weight_3 -= learning_rate * dw3


        
        
if __name__ == '__main__':
    data = pd.read_csv('Neuronne/Dataset/Iris.csv')

    data = pd.get_dummies(data , columns = ['Species'])

    data["Species_Iris-setosa"] = data["Species_Iris-setosa"].apply(lambda x: 1 if x else 0)
    data["Species_Iris-versicolor"] = data["Species_Iris-versicolor"].apply(lambda x: 1 if x else 0)
    data["Species_Iris-virginica"] = data["Species_Iris-virginica"].apply(lambda x: 1 if x else 0)

    train_data , test_data = train_test_split(data , test_size = 0.2 , random_state = 0)

    train_inputs , train_output = np.array(train_data[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]) ,np.array(train_data[['Species_Iris-setosa','Species_Iris-versicolor','Species_Iris-virginica']]).reshape((120,3))#type:ignore
    test_inputs , test_output = np.array(test_data[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]) ,np.array(test_data[['Species_Iris-setosa','Species_Iris-versicolor','Species_Iris-virginica']]).reshape((30,3))#type:ignore
    
    
    nn = NeuralNetwork(hidden_layer_1=20 ,hidden_layer_2=20)
    epochs = 100000
    learning_rate = 0.01
    cost = []
    for i in range(epochs):
        output = nn.feedforward(train_inputs)
        nn.backpropagation( train_inputs , output , train_output) 
        cost.append(nn.RSME(output,train_output))

    w1 , w2 ,w3 =nn.weight_1 ,nn.weight_2 ,nn.weight_3
    plt.plot(cost)
    plt.show()
    output = nn.feedforward(train_inputs)
    print(f'the loss = {1 - nn.RSME(output,train_output)}')
    print('testing phase')
    output = nn.feedforward(test_inputs)
    print(f'the loss = {1 - nn.RSME(output,test_output)}')
    print('end of script')