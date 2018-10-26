
# coding: utf-8

# In[15]:


print("***Currency Converter Program***")
print("1. Jordanian Dinar")
print("2. Turkish Lira")
print("3. US Dollars")

currencies = ["Jordanian Dinar", "Turkish Lira", "US Dollars"]

value = float(input("Inter the value to be converted: "))
from_Concurrency = int(input("From:(1/2/3) "))
to_Concurrency = int(input("To:(1/2/3) "))

JoD_UsD = 1.41
JoD_TuL = 7.88

converted_value = value
if from_Concurrency < 1 or from_Concurrency > 3 or to_Concurrency < 1 or to_Concurrency > 3 or value < 0 :
    print("Invalid Values!!")
else :
    if from_Concurrency == 2:
       converted_value =  converted_value / JoD_TuL
    elif from_Concurrency == 3:
       converted_value =  converted_value / JoD_UsD
    
    if to_Concurrency == 2:
       converted_value =  converted_value * JoD_TuL
    elif to_Concurrency == 3:
       converted_value =  converted_value * JoD_UsD
    
    print(value, currencies[from_Concurrency-1], "equals", converted_value, currencies[to_Concurrency-1])

