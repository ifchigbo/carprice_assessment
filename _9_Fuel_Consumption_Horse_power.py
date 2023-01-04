from matplotlib import pyplot as plt
from getDatPDDF import getChartVariables
from getDatPDDF import getHorsePower #3b
from getDatPDDF import getDataColumns #3B
from IPython.display import display
import numpy as np


def getBarChart():
    chart_var= getChartVariables()
    try:
        fig,(ax1,ax2) = plt.subplots(2,1,figsize=(15, 20))
        x = [fuelsystem for fuelsystem in chart_var['fuelsystem']]
        y = [car_count for car_count in chart_var['car_ID']]

        ax1.set(title="Car Fuel System Visualization",xlabel="Fuel System", ylabel="Total Car Count")
        ax1.bar(x,y)
        ax1.grid(True,alpha=0.5, linestyle='--', color='gray')
        ax1.set_facecolor('whitesmoke')
        ax1.grid(True,alpha=0.5, linestyle='--', color='gray')

        cols = getDataColumns()
        myhorse_power = getHorsePower()
        horse_power_T5 = myhorse_power.head(5)[[cols[1],cols[16],cols[19]]] #Top five cars with least price
        xh = [horse_p for horse_p in horse_power_T5['horsepower']]
        yh = [cost for cost in horse_power_T5['price']]
        ax2.set(title="Horse of the Top 5 Cars (Cheapest in Price)",xlabel="Car Horse Power",ylabel="Price of Car")
        #ax2.bar(xh,yh)
        ax2.plot(xh,yh,marker='o',linestyle="dotted")
        ax2.set_facecolor('whitesmoke')
        ax2.grid(True,alpha=0.5, linestyle='-', color='gray')
        plt.show()

        display(chart_var,myhorse_power.head(5)[[cols[1],cols[16],cols[19]]])
    except BaseException as error:
        print(error)


    