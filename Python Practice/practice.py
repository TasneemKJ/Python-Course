
# coding: utf-8

# In[5]:


x = int(input("Enter a number: "))
if x < 0 :
    g = -x
elif x < 100 :
    g = x**2 + 3*x - 5
else:
    g = (3/4) * x**3
    
print("g= ", g)

