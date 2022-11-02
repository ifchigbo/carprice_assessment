# import required modules and libraries for our analysis 
import os
import csv
import pandas as pd

#This function is responsible for loading data to memory

df_header=[]
data_set = []

def loadDatatoMemory():
    try:
        my_file = os.path.relpath("./CarPrice.csv")
        #get a collection of all data set columns and store in the list below
        with open(my_file,mode="r") as mydatafile:
            myopenfile = csv.reader(mydatafile)
            for headers in next(myopenfile):
                df_header.append((headers))
            for items in myopenfile:
                data_set.append((items))
    except BaseException as error:
        print("The Following Error occured: {} ".format(error))

loadDatatoMemory()

