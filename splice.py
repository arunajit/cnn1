from seq_reader import load_data             
from ohv import get_rep_mats, conv_labels  
import numpy as np
from sklearn.model_selection import StratifiedKFold     
from keras.datasets import mnist
from keras.layers import Dense, Dropout, Activation, Flatten, Convolution2D, MaxPooling2D
from keras.models import Sequential
from keras.utils import np_utils



seed = 123          
np.random.seed(seed)
X, y = load_data("data.txt")   
X = get_rep_mats(X)    
for i in X:             
    for idx, j in enumerate(i):
        i[idx] = j[0]
y = conv_labels(y)      
X = np.asarray(X)       
Y = np.asarray(y)	


kfs = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
scores = []

for train, test in kfs.split(X, Y):
    print ("----> FOLD [" + str(len(scores) + 1) + "]")


    Xtr = X[train].reshape(X[train].shape[0], 1,58, 64)
    Xts = X[test].reshape(X[test].shape[0], 1,58, 64)
    Xtr = Xtr.astype('float32')
    Xts = Xts.astype('float32')

    
    Ytr = np_utils.to_categorical(Y[train], 3)   
    Yts = np_utils.to_categorical(Y[test], 3)

    mod = Sequential()

    mod.add(Convolution2D(60, 3, strides=3, activation='relu', input_shape=(1, 58, 64), data_format='channels_first'))
    print (mod.output_shape)
    mod.add(MaxPooling2D(pool_size=(2,2)))
    mod.add(Dropout(0.25))

    mod.add(Flatten())
    mod.add(Dense(128, activation='relu'))
    mod.add(Dropout(0.5))
    mod.add(Dense(3, activation='softmax'))

    mod.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    
    mod.fit(Xtr, Ytr,validation_data=(Xts,Yts),
                  batch_size=32, nb_epoch=1, verbose=1)

    
    score = mod.evaluate(Xts, Yts, verbose=1)
    scores.append(score[1]*100)     
    print ("\n Score = " + str(score))


print("Min: %.2f%%, Average: %.2f%% (+/- %.2f%%), Max: %.2f%%" % (np.min(scores), np.mean(scores), np.std(scores), np.max(scores)))

