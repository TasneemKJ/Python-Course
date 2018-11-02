
# coding: utf-8

# In[7]:


import requests

link = "https://api.openweathermap.org/data/2.5/forecast"
city = input("Enter city(e.g: Amman,Jo): ")

additional_data = {
    "APPID" : "7bd564fc6c9bbb43d62c03c2585a9c91",
    "q": city,
    "units" : "metric"
}

data = requests.get(link,params=additional_data).json()

print(data)

