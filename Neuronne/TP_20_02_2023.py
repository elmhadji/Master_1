from tensorflow.keras import optimizers #type:ignore
from tensorflow.keras.models import Sequential #type:ignore
from tensorflow.keras.layers import Dense #type:ignore
import numpy as np 
from tensorflow import keras

X_or = [[0,0],
     [0,1],
     [1,0],
     [1,1]]
Y_or = [0,
     1,
     1,
     1]
modele = Sequential()
modele.add(Dense(units=2 , input_dim=2 , activation='relu'))
modele.add(Dense(units=16 , activation='relu'))
modele.add(Dense(units=1  , activation='linear'))

modele.compile(loss='mean_squared_error', optimizer='sgd')
print(modele.summary())

history = modele.fit(X_or, Y_or, epochs=1000, batch_size=100)