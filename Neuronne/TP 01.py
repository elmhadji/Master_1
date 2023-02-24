import numpy as np 

def segmoid(x):
    return 1/(1+np.exp(-x))

def error(yd , yp):
    return (1/2)*(yd - yp)**2

def s(x1 ,x2 ,w1 ,w2 ,b):
    return x1*w1 + x2*w2 +b

def os (s):
    return segmoid (s)

def dldE_y (yp ,yd):
    return yp -yd

def dldY_S (S):
    return (np.exp(S))/(np.exp(S)+1)**2




def dldE_W (a ,b ,c):
    return a*b*c


weight = [0.5 , 0.2 , 1.83]



# y = 0.03

# X = [0.1 , 0.3 ]

# weight = np.array(weight).T
# X = np.array(X).T

x1 = 0.1
x2 = 0.3

X =[x1 ,x2]

y=0.03

w1 = 0.5
w2 = 0.2
w3 = 0.62
w4 = 0.2
w5 = -0.2
w6 = 0.3

weight = [
    0.5,    #w1
    0.2,    #w2
    0.62,   #w3
    0.2,    #w4
    -0.2,   #w5
    0.3     #w6
]

baise = [
    0.4,
    -0.1,
    1.83
]

b1 = 0.4
b2 = -0.1
b3 = 1.83


def forward (X , weight , baise):

    OS1 = os(s(X[0] , X[1] , weight[0] , weight[2] , baise[0]))

    OS2 = os(s(X[0] , X[1] , weight[1] , weight[3] , baise[1]))

    OS3 = os(s(OS1 , OS2 , weight[4] , weight[5] , baise[2]))

    return OS1 ,OS2 , OS3

OS1 , OS2 , OS3 = forward(X ,weight , baise)



    
weight[0] = weight[0] + 0.01 * dldE_W(dldE_y(OS3 ,y) ,dldY_S())
    


# def freed_forward(x1 , x2 ,w1, w2 ,w3 ,w4 ,w5 ,w6 ,b1 ,b2 ,b3):
#     global OS1,OS2,OS3
#     OS1= os(x1 ,x2 ,w1 ,w3 ,b1)

#     OS2= os(x1 ,x2 ,w2 ,w4 ,b2)
    
#     OS3 = os(OS1 ,OS2 ,w5 ,w6 ,b3)
    
    
#     return OS3


# print(freed_forward(x1, x2 ,w1 ,w2 ,w3 ,w4 ,w5 ,w6 ,b1 ,b2 ,b3))
# print(error(y ,freed_forward(x1, x2 ,w1 ,w2 ,w3 ,w4 ,w5 ,w6 ,b1 ,b2 ,b3)))


    










 
