#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:04:30 2022

@author: asus
"""
#imported modules
import pandas as pd
import matplotlib.pyplot as plt


def lineplot() :
    """
     function for multiline plot for showing birth rates in 1985, 1963, 2002

    """
    
    plt.figure(figsize = (10,12))
    plt.plot(data["Country Name"], data["1960"], 
         label = "1985")
    plt.plot(data["Country Name"], data["1970"], 
         label = "1963")
    
    plt.xlabel("CountryCode")
    plt.ylabel("Survival to age 65")
    plt.legend()
    plt.title("multiline plot showing survival to age 65 rate")
# saving figure
    plt.savefig("linegraph.png")
    plt.show()
    


def barChart() :
    """
    Function for the bar chart for plotting the birth rate in 1986 and 2015
    """

    plt.figure(figsize = (10,10))

    plt.bar(data["Country Name"], data["1960"], 
            label = "1960", alpha = 1.0, color = 'red')
    plt.bar(data["Country Name"], data["2015"], 
            label = "2015", alpha=0.6, color = 'black')
   
   
    plt.xlabel("Country Name")
    plt.xticks(rotation=90)
    plt.ylabel("Survival to age 65")
    plt.title("Bar graph showing survival to age 65 rate")

    plt.savefig("barchart_png")
    plt.legend()
    plt.show()
    


def barSub() : 
    """
     Function for the bar with subplots showing changes in 2015 and 2016. 
    """
   
    plt.figure(figsize = (10,13))
    

    plt.subplot(2, 2, 1)
    plt.subplots_adjust(left=0.1, bottom= 0.1, right=0.9,top= 1.0,wspace=0.4,hspace=0.4)
    plt.bar(data["Country Name"], data["1960"], 
            label = "1960", alpha = 1.0, color = 'violet')
    plt.xticks(rotation=90)
    plt.title("Bar graph showing showing survival to age 65 rate in 2015 ")
    plt.xlabel("Country Name")
    plt.ylabel("Survival to age 65")
    plt.legend()
     
    plt.subplot(2, 2, 2)
    plt.bar(data["Country Name"], data["2020"], 
            label = "2020", alpha = 1.0, color = 'green')
    plt.xticks(rotation=90)
    plt.xlabel("Country Name")
    plt.ylabel("Survival to age 65")
    plt.title("Bar graph showing showing survival to age 65 rate in 2020")
    plt.savefig("barchart_png1")
    plt.legend()
    plt.show()
    


def box() :
    """
    Function for the box plot for plotting the birth rate in 1986 and 2015
    """

# plot the figure
    plt.figure(figsize = (8,9))
    plt.boxplot([data["1960"],
                 data["2020"],
                ], 
                labels = ["1960",
                          "2020",
                         ])
 
# set labels and show the legend
    plt.xlabel("Box plot showing survival to age 65 rate in 1960 and 2020")
    plt.ylabel("Survival to age 65")
    plt.title("Box plot showing survival to age 65 in 1960 and 2020")
    plt.savefig("boxfig_png")
    plt.legend()
    plt.show()
    

# read file into dataframe and print
data = pd.read_csv("roshan.csv")
print(data)

lineplot()
barChart()
barSub()
box()