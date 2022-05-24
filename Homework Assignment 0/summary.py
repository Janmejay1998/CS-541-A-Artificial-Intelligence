#Author: Janmejay Mohanty
#Cite: https://stackoverflow.com/questions/24023927/computing-standard-deviation-without-packages-in-python
from numpy import greater
import pandas as pd

state = input("\nEnter the US State (example : Illinois, first letter should be uppercase) : ")            #User Input

df = pd.read_csv("us-states.csv")                                    #Loading CSV file into Python code
newdf = df[df['state'] == state]

n1 = pd.DataFrame(newdf, columns= ["date","state", "cases"])

print (n1)

def max_min(lst):                                                     #Maximum and Minimum Function
    lst = map(int,lst)
    lst = list(lst)

    greater = lst[0]
    lesser = lst[0]
    for num in lst:
        if num> greater:
            greater = num
        elif num< lesser:
            lesser = num
    print("\nMaximum cases = ", greater, "and Minimum cases = ", lesser)


def mean_stddv(lst):                                                   #Mean and Standard Deviation
    total = 0
    for i in lst:
        total = total + i
    mean = total / len(lst)

    TOTAL = 0
    for i in lst :
        TOTAL +=(i-mean)**2
    stddv = (TOTAL/(len(lst)-1))**0.5 
    print("\nMean = ",round(mean,2),"and Standard Deviation = ", round(stddv,2), "\n")
      

c = n1['cases']  

max_min(c)                          # Printing Maximum and Minimum cases
mean_stddv(c)                       # Printing Mean and Standard Deviation



