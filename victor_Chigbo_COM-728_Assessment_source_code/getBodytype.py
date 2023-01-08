from getDatPDDF import getCarasPDDF
from loaddata import df_header, data_set

def getUniqueBodyType():
    try:
        body_types = [body[4] for body in data_set] # get all the data on the 4 column that represents the car body type
        # get the unique body type from the list above
        unique_body_type = [items for items in set(body_types)] # Get unique body type using the set function and assign the result to a list
        return unique_body_type #return value of the function is a list of unique car body type
        
    except BaseException as error:
        print("The following error has occured: {}".format(error))



