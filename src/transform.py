# transform
# should be minimal transformation required considering the data set, will learn more as I go
# okay making sense of, and transforming, the dataset will require some work. I have no experience with the IDX file format.
# the dataset can be found on kaggle as a csv,
# as the purpose of this excercise is more so to understand NN than the IDX file format, I'll be downloading that instead of transforming

# lets write the format of the data
# each row of the csv file represents 1 picture, apart from the first row which gives column names
# order is that each row of the file itterates through every column in the first of the image, then second, then third etd
# or, i*j, itterate through j 1-28 then increment i

# in what format do we want it?
    # one suitable for matrix multiplication
    # lets trim the labels and maybe take the transpose?

def transform():
    pass