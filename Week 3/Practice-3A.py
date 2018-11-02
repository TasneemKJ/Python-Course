
# coding: utf-8

# In[1]:


import requests


# In[2]:


#Forex APIS from https://fixer.io/
def available_rates():
    base_link_latest = 'http://data.fixer.io/api/latest'
    parameters_latest = {
        "access_key" : "e1be8ec55a7c5fa9600ff656adf94ac4",
    }
    response_latest_rates = requests.get(base_link_latest,parameters_latest).json()
    return response_latest_rates['rates']

def available_curr():
    return list( available_rates().keys())

def get_rate(curr):
    return float(available_rates()[curr])


# In[3]:


available_currencies = available_curr()

print("Avaialabe Currencies: ",available_currencies)
base_curr = input("Choose a currency: ")
available_currencies.remove(base_curr)

print("Available to: ", available_currencies)
to_curr = input("Choose from the above: ")

amount = float(input("How many you want to convert: "))
result = (get_rate(to_curr)/get_rate(base_curr)) * amount

print(f"{amount} {base_curr} to {to_curr} is {result}") 

