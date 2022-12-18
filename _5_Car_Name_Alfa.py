from getDatPDDF import getCarNames
from IPython.display import display
#This method calls the getCarNames function from the getDataPDDF module
#It retrieves the cleaned data that returns the Car names in alphabetical order
def sortCarbyAlph():    
    try:
        names = getCarNames()
        display(names)
    except BaseException as error:
        print("The following error occured: {}".format(error))

if __name__ == '__main__':        
    print(sortCarbyAlph())
