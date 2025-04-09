# import
# Decide whether to import from website or csv, just learnt some basic webscraping so I still find that interesting and exciting
# I'm going to import from a csv included in the program files
# May be 4 csvs in 1 cvs so extra transformation required

import pandas as pd

def extract():
    raw_test_data = pd.read_csv('../dataset/mnist_test.csv')
    raw_training_data = pd.read_csv('../dataset/mnist_train.csv')
    return raw_test_data, raw_training_data
