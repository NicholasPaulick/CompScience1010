import math

x = int(input("Enter time in seconds: "))
print("")

hr = math.trunc(x/3600)
min = math.trunc((x//60) % 60)
sec = math.trunc(x%60)

print("Hours: " + str(hr))
print("Minutes: " + str(min))
print("Seconds: " + str(sec))