import numpy as np
from random import random
from sklearn.model_selection import train_test_split
import tensorflow as tf

def generate_dataset(sample_size,test_size):
    x = np.array([[random()/2 for _ in range(2)] for _ in range(sample_size)])
    y = np.array([[i[0]+i[1]] for i in x])
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=test_size)
    return x_train, x_test, y_train, y_test

if __name__=="__main__":
    x_train, x_test, y_train, y_test = generate_dataset(10,0.2)

    #model definition
    model = tf.keras.Sequential(
        [
         tf.keras.layers.Dense(5,input_dim=2,activation="sigmoid"),
         tf.keras.layers.Dense(1,activation="sigmoid")
        ]
    )
    #compile model
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.1)
    model.compile(optimizer=optimizer,loss="MSE")

    #train model
    model.fit(x_train,y_train,epochs=1000)

    #test model
    model.evaluate(x_test,y_test,verbose=1)

    #predict
    data = np.array([[0.1,0.2],[0.3,0.4]])
    prediction= model.predict(data)

    #results
    for d,p in zip(data,prediction):
      print("{}+{}={}".format(d[0],d[1],p))



