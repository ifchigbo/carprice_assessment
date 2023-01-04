from loaddata import df_header, data_set
from getDatPDDF import getCarasPDDF
import pandas as pd
from IPython import display


#Get Car value by ID
def getCarbyID():
    # I am using this check to keep track of  index in my records index
    checker  = 1
    try:
        id = int(input("Enter the ID of the Car you want to view: "))
        # index in a list starts from zero, but the car index starts from one , so i need to subtract id  from my checker variable
        id = id - checker
        return data_set[id][:] # return the list of car records  according to the input id - id = id - checker
    except BaseException as error:
        print("Your Error Message reads: {}".format(error))


def displayCarDataQuerybyID():
    # the block below is ussed to display each column header and the the corresponding value of the header based on the input ID
    try:
        car_id_details = []
        for items in getCarbyID(): #function is called based on the method defined above
            car_id_details.append(items)
        car_record = zip(df_header,car_id_details) # the zip function is used to create a dictionary of the data column header and the corresponding records associated to the column header
        
        for ID,car_details in  dict(car_record).items():
           print("The {} of the car is: {}".format(ID,car_details)) #print the result in form of a text  statement
    except BaseException as error:
        print("The following error occured: {}".format(error))

