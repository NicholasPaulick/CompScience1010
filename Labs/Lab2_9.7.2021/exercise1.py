# 1. You have been tasked with creating a time converter program. 
#    This program will require you to first ask the users for a time in seconds (e.g 2500 seconds) using the prompt “Please enter a number of seconds:” Once the program receive the input, the program will then calculate the number of hours based on the input number. 
#    In addition, the program will also figure out the remainder of minutes and seconds that are left within the initially identified time after the time has been converted into hours (e.g if the time given was 7265 seconds, then the remainder after the conversion will be one minute and 5 seconds). 
#    After the conversion been completed, your program will print out the results using the following sentences:
#       a) Here is the time in hours, minutes, and seconds
#       b) Hour: X
#       c) Minutes: Y
#       d) Seconds: Z 

import math

x = int(input("Enter time in seconds: "))
print("")

hr = math.trunc(x/3600)
min = math.trunc((x//60) % 60)
sec = math.trunc(x%60)

print("Hours: " + str(hr))
print("Minutes: " + str(min))
print("Seconds: " + str(sec))