#This module gets the data set as a pandas DF
import pandas as pd
from loaddata import my_file
from loaddata import df_header # call header columns
#method to get dataframes
def getCarasPDDF():
    try:
        # load  data frame using the pandas library
        dataframe =pd.read_csv(my_file)
        return dataframe #return statement for the data frame variabl
    except BaseException as  error:
        print(error)


#method to get data frame columns 
def getDataColumns(): # get the list of data frame columns
    try:
        columns = [col for col in getCarasPDDF().columns]
        return columns
    except BaseException as error:
        print("The following error occured: {}".format(error))

def getCarNames():
    car_names = getCarasPDDF()
    try:
        #get car names  from header variable from loaddata module
        # Convert the columns data under car name from to string and then convert all records on the column to lower case
        # This eliminate any record that is upper case or starts in upper case - validate that values on the CarName column are all lower case
        car_names[df_header[1]] = car_names[df_header[1]].str.lower()
        return car_names.sort_values(df_header[1]) # return the result of the manipulation
        #return car_names
    except BaseException as error:
        print("The following error occured: {}".format(error))