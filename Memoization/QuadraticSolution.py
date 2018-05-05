#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 23:31:46 2017

@author: pawan
"""
import timeit

# Function to return the number of times a number can be written as a sum of 1,3 and 4
def parts(n):
    if n == 0 or n ==1 or n == 2:
        return 1
    elif n == 3 :
        return 2
    elif n == 4 :
        return 4
    else:
        return parts(n-1) + parts(n-3) + parts(n-4)

try:
    number = int(input("\nEnter a number that you want to know how many times it can be written as sum of 1,3 and 4 :: "))
    
    #Get the start time
    start = timeit.default_timer()
        
    result = parts(number);
    
    #Get the end time
    stop = timeit.default_timer()
    
    print (stop - start)
    
    print("\n\nThe number",number,"can be wriiten as a sum of 1,3 and 4 in -->",result,"of way(s)")
    #print("\n\nThe number",number,"can be wriiten as a sum of 1,3 and 4 in -->",result,"of way(s). \
    #      \n\n\n**** Note **** - You will have really really long numbers for your output. for example, if your input is 10,000, then your output will have more than 20,000 DIGITS). So just need to print the last 5 digits for each output. ")

except ValueError:
    print("\nPlease provide a positive integer numbers only.")
    exit


'''
::::::::::::::::::::: OUTPUT :::::::::::::::::::::
Number      Last 5 digits of the output 
50      --->>60449
100     --->>33476
200     --->>78201
500     --->>58001
1000    --->>87876
100000  --->>71876
100001  --->>78126
100002  --->>50001
100003  --->>28127
100004  --->>78129
100500  ---->>83001
100600  ---->>41476
100900  ---->>6276


50      --->>60449
100     --->>33476
200     --->>78201
1000    --->>87876
110001  -->>4376
100000  --->>71876
100001  --->>78126
200034  --->>17681

'''