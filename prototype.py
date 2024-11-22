import numpy as np
import pandas as pd
import matplotlib as plt

# import and transform the data
# probably using pandas

# import
# Decide whether to import from website or csv, just learnt some basic webscraping so I still find that interesting and exciting
# I'm going to import from a csv included in the program files
# May be 4 csvs in 1 cvs so extra transformation required

df = pd.read_csv('Neural_Nets/3b1bnumpy/Programs/mnist_test.csv')

# transform
# should be minimal transformation required considering the data set, will learn more as I go
# okay making sense of, and transforming, the dataset will require some work. I have no experience with the IDX file format.
# the dataset can be found on kaggle as a csv,
# as the purpose of this excercise is more so to understand NN than the IDX file format, I'll be downloading that insteas of transforming

# structure
# input is 28*28 grayscale pixels(0-255?), thus 784 input neurons
# 2 hidden layers of 16
# 10 output neurons
# starting to set in that this may be a more laborious task than anticipated, but I guess that gives me motivation to learn how to code it efficiently
# maybe not, numpy has good functions

# structure - random
# way to randomly assign initial weights for each layer
# '''
# 
# '''
# create
# a matrix with size ? and populate it with random numbers between ? and ?
# np.random.rand
# np.multiply(mmatrix1,mmatrix2)

# loss function
# function I want to minimize. 
# Iirc its the sum (ITS THE AVERAGE) of the square of the differences between the wanted values (0, 1) for each digit, 
# and the actual values obtained minus a bias (for improved edge detection)

# activation function
# reLU and/or sigmoid
# return 1/(1+np.exp(-X))

# method for backpropogation
# can't remember the calculus, will need to refer to the video
# backpropogation uses SGD no? (This example just uses GD) so should be fairly straightforward, though not short
# need a way to turn backpropogation off during testing?

