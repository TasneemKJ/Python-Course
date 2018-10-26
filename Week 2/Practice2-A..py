
# coding: utf-8

# In[29]:


import math as mt

print("This program prints the first n prime numbers")
n = int(input("Enter n: "))

if n < 1:
    print("Invalid n value")
else:
    count = 0
    num = 1

    while(count < n):
        prime = True;
        for i in range(2, int(mt.sqrt(num)+1)):
            if num % i == 0:
                prime = False
                break
        if prime == True:
            print(num)
            count = count + 1
        num = num + 1

