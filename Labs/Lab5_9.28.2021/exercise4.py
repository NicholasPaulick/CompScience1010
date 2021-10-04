def prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print("{num}\tnot prime".format(num=num))
                break
        else:
            print("{num}\tprime".format(num=num))
    
    else:
        print("{num}\tnot prime".format(num=num))


print("number\tis prime")
print("-------------------")

for num in range(100):
    prime(num + 1)