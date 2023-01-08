from getDatPDDF import getCarNames
from loaddata import df_header
#This method calls the getCarNames function from the getDataPDDF module
#It retrieves the cleaned data that returns the Car names in alphabetical order
def sortCarbyAlph():    
    try:
        names = getCarNames()
        print("Displaying the first 50 reccords .................")
        print(names[df_header[1]].head(50))
        print("\n")
        print("Displaying the last 50 records ...................")
        print(names[df_header[1]].tail(50))
    except BaseException as error:
        print("The following error occured: {}".format(error))


