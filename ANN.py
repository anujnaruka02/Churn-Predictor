# For first confusion matrix
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([keras.layers.Dense(20, input_shape = (26,), activation = 'relu'),
                         keras.layers.Dense(1, activation = 'sigmoid')])

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

model.fit(X_train, Y_train, epochs = 50)

model.evaluate(X_test, Y_test)

# For second confusion matrix
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([keras.layers.Dense(20, input_shape = (26,), activation = 'relu'),
                         keras.layers.Dense(1, activation = 'sigmoid')])

model.compile(optimizer = 'adagrad', loss = 'binary_crossentropy', metrics = ['accuracy'])

model.fit(X_train, Y_train, epochs = 50)

model.evaluate(X_test, Y_test)

