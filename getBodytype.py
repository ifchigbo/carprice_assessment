from getDatPDDF import getCarasPDDF
from loaddata import df_header, data_set

def getUniqueBodyType():
    try:
        body_types = [body[4] for body in data_set]
        # get the unique body type from the list above
        unique_body_type = [items for items in set(body_types)]
        return unique_body_type
        
    except BaseException as error:
        print("The following error has occured: {}".format(error))

getUniqueBodyType()