
# coding: utf-8

# In[7]:


states = ["Ma'an", "Irbid", "Muhafazat az Zarqa'", "Muhafazat at Tafilah", "Amman Governorate", "Al Mafraq", "Al Karak", "Muhafazat al Balqa'", "Ajloun", "Jerash", "Muhafazat al 'Aqabah", "Muhafazat Ma'daba"]

print("***states that start with a***")
for i in range(0, len(states)):
    if states[i].lower().startswith("a"):
        print(states[i])
        
print("\n***states of lenght 5***")
for i in range(0, len(states)):
    if len(states[i]) == 5:
        print(states[i])

