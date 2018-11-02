
# coding: utf-8

# In[21]:


import os,sys
           
def list_files_pre(pre, path):
    print(pre, path)
    files = os.listdir(path)
    for name in files:
        if os.path.isdir(path + '\\' + name):
            list_files_pre(pre+" ", path + '\\' + name)
        else:
            print(pre+" ", "-", name)

            
def list_files(path):
    list_files_pre('   ', path)
    
    
path = input("Enter the path you want to list: ")
list_files(path)

print("Enter the path of the file you want to rename: ")
print("e.g: C:\\Users\\Tasnim\Desktop\\list")
path_rename = input("PATH: ")
print("Enter the name of the file you want to rename: ")
print("e.g: file1.txt")
file = input("FILE: ")
print("Enter the new name of the file you want to rename: ")
print("e.g: file2.txt")
name = input("NAME: ")

print(f'Renaming file {path_rename} \\ {file} to {name} ...')
os.rename(path_rename + '\\' + file, path_rename + '\\' + name)
print(f'file {path_rename} \\ {file} renamed to {name}')

list_files(path)

