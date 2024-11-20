import numpy as np

# import and transform the data
# probably using pandas

# import
# Decide whether to import from website or csv, just learnt some basic webscraping so I still find that interesting and exciting
# I'm going to import from a csv included in the program files


# transform
# should be minimal transformation required considering the data set, will learn more as I go
# okay making sense of, and transforming, the dataset will require some work. I have no experience with the IDX file format.
# the dataset can be found on kaggle as a csv,
# as the purpose of this excercise is more so to understand NN than the IDX file format, I'll likely be downloading that insteas of transforming

# structure
# input is 28*28 grayscale pixels(0-255?), thus 784 input neurons
# 2 hidden layers of 16
# 10 output neurons
# starting to set in that this may be a more laborious task than anticipated, but I guess that gives me motivation to learn how to code it efficiently
# way to randomly assign initial weights

# loss function
# function I want to minimize. 
# Iirc its the sum (ITS THE AVERAGE) of the square of the differences between the wanted values (0, 1) for each digit, and the actual values obtained minus a bias (for improved edge detection)

# activation function
# reLU and/or sigmoid

# method for backpropogation
# can't remember the calculus, will need to refer to the video
# backpropogation uses SGD no? (This example just uses GD) so should be fairly straightforward, though not short

