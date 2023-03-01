import numpy as np
from tensorflow import keras
from tensorflow.keras import optimizers #type:ignore
from tensorflow.keras.models import Sequential #type:ignore
from tensorflow.keras.layers import Dense #type:ignore
import matplotlib.pyplot as plt

# Partie A. Données
# Fonction à approcher
def f(x):
        return np.cos(2*x) + x*np.sin(3*x) + x**0.5 - 2

a, b = 0, 5 # intervalle [a,b]
N = 100 # taille des données
X = np.linspace(a, b, N) # abscisses
Y = f(X) # ordonnées
X_train = X.reshape(-1,1)
Y_train = Y.reshape(-1,1)

# Partie B. Réseau
modele = Sequential()
modele.add(Dense(10, input_dim=1, activation='tanh'))
modele.add(Dense(10, activation='tanh'))
#modele.add(Dense(10, activation='tanh'))
modele.add(Dense(10, activation='tanh'))
modele.add(Dense(1, activation='linear'))

# Méthode de gradient : descente de gradient classique
#mysgd = optimizers.SGD(learning_rate = 0.001, decay=1e-7, momentum=0.9, nesterov=True)
#learning_rate = 0.01, momentum = 0.0, nesterov = False
modele.compile(loss='mean_squared_error', optimizer='sgd')
print(modele.summary())

# Partie C. Apprentissage
history = modele.fit(X_train, Y_train, epochs=30000, batch_size=N)

# Partie D. Visualisation
# Affichage de la fonction et de son approximation
Y_predict = modele.predict(X_train)
plt.plot(X_train, Y_train, color='blue')
plt.plot(X_train, Y_predict, color='red')
plt.show()

# Affichage de l'erreur au fil des époques
plt.plot(history.history['loss'])
plt.show()

