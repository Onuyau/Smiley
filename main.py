import tensorflow as tf
from tensorflow import keras
#from keras import regularizers
import numpy as np
import matplotlib as plt
#from numpy import exp, array, random, dot
# from keras.models import Model
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import SGD
from keras.utils import to_categorical
#from sklearn.model_selection import train_test_split
print(keras.__version__)

INIT_LR = 0.01
EPOCHS = 100
seed = 5
np.random.seed(seed)

x_train = np.array([[0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                   [0,  0,  0,  0,  1,  1,  0,  0,  0,  0],
                   [1,  1,  0,  0,  0,  0,  0,  0,  0,  0],
                   [1,  0,  1,  0,  1,  0,  0,  0,  0,  0],
                   [0,	0,	1,	1,	0,	0,	1,	0,	0,	0],
                   [1,	1,	0,	1,	0,	0,	0,	0,	1,  0],
                   [0,	0,	0,	1,	0,	1,	0,	1,	0,	0],
                   [1,	1,	0,	1,	0,	1,	0,	0,	0,	0],
                   [1,	1,	0,	1,	0,	1,	0,	1,	0,	0],
                   [1,	1,	1,	1,	1,	0,	0,	0,	0,	0],
                   [0,	1,	0,	0,	0,	1,	1,	1,	1,	0],
                   [1,	1,	0,	1,	1,	1,	1,	0,	0,	0],
                   [1,	0,	0,	1,	0,	1,	1,	0,	1,	0],
                   [1,	0,	1,	0,	1,	0,	0,	1,	1,	0],
                   [0,	0,	1,	1,	0,	1,	0,	1,	1,	0],
                   [1,	0,	1,	0,	1,	0,	0,	1,	0,	1],
                   [1,	1,	1,	0,	1,	0,	1,	0,	0,	0],
                   [1,	1,	1,	1,	1,	0,	0,	0,	0,	0],
                   [0,	1,	1,	1,	0,	0,	0,	1,	1,	0],
                   [0,	1,	1,	0,	1,	1,	1,	0,	1,	0],
                   [1,	1,	0,	1,	0,	0,	1,	0,	1,	1],
                   [0,	1,	0,	1,	1,	1,	1,	1,	0,	1],
                   [0,	0,	1,	1,	1,	1,	1,	1,	1,	0],
                   [1,	1,	1,	1,	1,	1,	1,	0,	0,	0],
                   [1,	1,	1,	1,	1,	1,	1,	1,	0,	0],
                   [0,	0,	1,	1,	1,	1,	1,	1,	1,	1],
                   [1,	0,	1,	1,	0,	1,	1,	1,	1,	1],
                   [1,	1,	1,	1,	1,	1,	1,	1,	0,	1],
                   [1,	1,	1,	1,	1,	1,	1,	1,	1,	0],
                   [1,	1,	1,	1,	1,	1,	1,	1,	1,	1]])

y_train = np.array([[1],  [1],  [1],  [2],  [2],  [2],  [2],  [2],  [3],  [3],  [3],  [3],  [3],  [3],  [3],  [3],  [3],  [3],  [3],  [3],  [4],  [4],  [4],  [4],  [4],  [5],  [5],  [5],  [5],  [5]]).T
#y_train = np.array([[1,  1,  1,  2,  2,  2,  2,  2,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,  5,  5]]).T


x_test = np.array([[1,	0,	0,	1,	0,	0,	0,	0,	0,	0],
                  [0,	0,	0,	0,	1,	0,	1,	0,	0,	0],
                  [1,	1,	1,	0,	1,	1,	1,	0,	1,	1],
                  [0,	1,	0,	1,	0,	1,	0,	0,	0,	1],
                  [1,	1,	1,	1,	0,	1,	1,	1,	0,	1],
                  [1,	1,	1,	0,	1,	1,	1,	1,	0,	0],
                  [1,	0,	0,	1,	1,	0,	1,	0,	0,	0],
                  [1,	1,	1,	1,	1,	0,	0,	1,	1,	1],
                  [0,	1,	0,	0,	1,	0,	1,	0,	1,	0],
                  [0,	0,	0,	1,	0,	1,	0,	1,	0,	0],
                  [1,	1,	0,	0,	1,	0,	1,	0,	1,	0],
                  [1,	0,	1,	1,	0,	1,	0,	1,	0,	1],
                  [1,	1,	0,	1,	1,	0,	1,	1,	1,	1],
                  [1,	1,	1,	1,	1,	1,	0,	1,	1,	1]])


y_test = np.array([[1],  [2],  [4],  [3],  [4],  [4],  [2],  [5],  [3],  [2],  [3],  [4],  [5],  [5]]).T
#y_test = np.array([[1,  2,  4,  3,  4,  4,  2,  5,  3,  2,  3,  4,  5,  5]]).T

print("x_train",x_train.shape)
print("y_train",y_train.shape)
print("x_test",x_test.shape)
print("y_test",y_test.shape)

opt = SGD(lr=INIT_LR)

# from sklearn.datasets import load_digits
# digits = load_digits()
# print(digits.data.shape)
# import matplotlib.pyplot as plt
# plt.gray()
# plt.matshow(digits.images[1])
# plt.show()
#
# digits.data[0,:]
#
# from sklearn.preprocessing import StandardScaler
# X_scale = StandardScaler()
# X = X_scale.fit_transform(digits.data)
# X[0,:]

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

#input_shape 10 входов, скрытый слой 10, 5 нейронов, выходной слой 5 нейронов
model = Sequential()
model.add(Dense(5, activation='relu', batch_size=5, input_dim=10 ))
#model.add(Dense(10, activation='relu', input_shape=(None,10) , batch_size=10 ))
#model.add(Dense(10, activation='relu'))
model.add(Dense(5, input_shape=(5,5),kernel_initializer='uniform', activation='relu'))
model.add(Dense(units=5, kernel_initializer='uniform', activation='sigmoid'))
#model.add(Dense(units=5, activation='relu'))

model.summary()

model.compile(optimizer=opt, loss='mse', metrics=['accuracy'])
#тренировка нейросети
history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=EPOCHS, batch_size=10)

model.evaluate(x_test, y_test, verbose=1)

# оцениваем нейросеть
print("[INFO] evaluating network...")
predictions = model.predict(x_test, batch_size=32)
print(classification_report(y_test.argmax(axis=1),
                            predictions.argmax(axis=1), target_names=lb.classes_))

# строим графики потерь и точности
N = np.arange(0, EPOCHS)
plt.style.use("ggplot")
plt.figure()
plt.plot(N, H.history["loss"], label="train_loss")
plt.plot(N, H.history["val_loss"], label="val_loss")
plt.plot(N, H.history["acc"], label="train_acc")
plt.plot(N, H.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy (Simple NN)")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.savefig(args["plot"])



#optimizer

pred = model.predict(x_predict)
print("Предсказанная оценка:", pred[1][0], ", Правильная оценка:", y_test[1])