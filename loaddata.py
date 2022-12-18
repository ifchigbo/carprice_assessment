#import required modules and libraries for our analysis
import os
import csv
import tui


#This function is responsible for loading data to memory
df_header=[]
data_set = []
my_file = os.path.relpath("./CarPrice.csv")

def loadDataSetasCSV():
    try:
        #get a collection of all data set columns and store in the list below
        tui.startModule("Loading CSV Data File ..........")
        with open(my_file,mode="r") as mydatafile:
            myopenfile = csv.reader(mydatafile)
            for headers in next(myopenfile):
                df_header.append((headers))
            for items in myopenfile:
                data_set.append((items))
        print("\n")
        tui.completed("Load Sequence Completed.")
    except BaseException as error:
        print("The Following Error occured: {} ".format(error))


loadDataSetasCSV() # calling this method is what populates the df_header and data_set list defined above
#print(data_set)