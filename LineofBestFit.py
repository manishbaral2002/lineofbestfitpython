# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:45:07 2020

@author: manis
"""


import csv
import numpy as np
import matplotlib.pyplot as plt

with open('XVAL.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  
    Xvalues = np.genfromtxt('XVAL.csv', delimiter = ',')
    print(Xvalues)
    #for line in csv_reader:
        #print(line)
    Yvalues = np.genfromtxt('YVAL.csv', delimiter = ',')
    print(Yvalues)
    
    plt.scatter(Xvalues,Yvalues)
    plt.show()
    
    #graph needs to be in a y=mx+b form where m is the slope and b is a y intercept, X and Y are their repective valuees. 
    #the general formula for line of best fit is summation of y values(yvaluesdot) times x values and then minus y mean multiplied by x summation
    #that is to be divided by the summation of xXi-xval mean times xvalues sum
    #for b it is mean of y values times the x values - x mean times y val and x val
    #then this is divided by summation of x values - mean of x values times sum of x values
    m = (Yvalues.dot(Xvalues) - Yvalues.mean()*Xvalues.sum()) / ( Xvalues.dot(Xvalues) - Xvalues.mean()* Xvalues.sum()  ) 
    b = ( Yvalues.mean() * Xvalues.dot(Xvalues) - Xvalues.mean() * Yvalues.dot(Xvalues)) / ( Xvalues.dot(Xvalues) - Xvalues.mean()* Xvalues.sum()  )


Lineofbestfit = m*Xvalues + b
plt.scatter(Xvalues,Yvalues)
plt.plot(Xvalues,Lineofbestfit)
plt.show()
   
#import csv
#line_number = 2
#with open('PythonTest.csv', 'rb') as f:
    #mycsv = csv.reader(f)
    #mycsv = list(mycsv)
    #text = mycsv[line_number][1]

