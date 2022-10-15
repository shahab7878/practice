#!/usr/bin/env python
# coding: utf-8

# # Q1
# > In _priceList.txt_ :
# >> the first line will contain the number of items in the file.
# >> Each subsequent line will contain:
# >>> the name of an item (as a string without spaces),
# >>> the cost of the item from Amazon (represented as a double),
# >>> the cost of the item from HyVee (represented as a double),
# >>>> like this: *itemName* *[amazonPrice]* *[hyveePrice]*
# 
# </br>
# 
# > Write a program to read the info contained in the *_priceList.txt_* file:  </br>
# >> 1. find the price for oatmeal at each store, and display the price difference between Amazon and HyVee.
# >> 2. separate the items that cost less than _$5_ from the items that cost more than _$5_.
# >> 3. display the names of the items that cost less than _$5_ and the names of the items that cost more than _$5_.
# >> 4. display the total number of items that cost less than _$5_ and the total number of items that cost more than _$5_.

# In[4]:


with open("priceList.txt", "r") as f:
    n = int(f.readline())
    priceList = []
    for _ in range(n):
        priceList.append(f.readline().split(" "))
        priceList[_][1] = float(priceList[_][1])
        priceList[_][2] = float(priceList[_][2])
priceList_5 = []
for _ in range(5):
    if priceList[_][0] == "oatmeal":
        print(f"the oatmeal price difference between two stores: {priceList[_][1] - priceList[_][2]}")
    if priceList[_][1] > 5 or priceList[_][2] < 5:
        priceList_5.append(priceList[_])
        
print([priceList_5[i][0] for i in range(len(priceList_5))])
print(len(priceList_5))


# # Q2
# > Write a program that get information from the user and write it to the *_info.txt_* file.
# >> The program should ask the user for the following information:
# >>> 1. the name of the person
# >>> 2. birth date
# >>> 3. phone number
# >>> 4. email address
# >>> 5. address
# >>> 6. city
# >>> 7. National ID number
# 
# Note: info should be written in the following format(each line is a separate record and info should be separated by spaces):
# > *name* *[birthDate]* *[phoneNumber]* *[emailAddress]* *[address]* *[city]* *[nationalID]*

# In[14]:


list_person = []
while True:
    p = {}
    p['name'] = input('name: ')
    p['birthDate'] = input('birthDate: ')
    p['phoneNumber'] = input('phoneNumber: ')
    p['emailAddress'] = input('emailAddress: ')
    p['address'] = input('address: ')
    p['city'] = input('city: ')
    p['ID'] = input('ID: ')
    list_person.append(p)
    leave = input("do you want to continue?(y/n): ")
    if leave == 'n':
        break
        
with open('info.txt', 'w') as f:
    temp = True
    for _ in list_person:
        if temp == True:
            for key, value in _.items():
                f.write(key)
                f.write(" ")
            f.write("\n")
            temp = False 
        for key, value in _.items():
            f.write(value)
            f.write(" ")
        f.write("\n")
    


# # Q3
# > Write a program based on output of `Q2` that:
# >> 1. reads the information from the *_info.txt_* file and display it.
# >> 2. ask the user for the name of the person and display the information for that person.

# In[16]:


with open('info.txt', 'r') as f:
    f.readline()
    list_person = f.readlines()

name = input("inter the name: ")
for _ in list_person:
    temp = _.split(" ")
    if temp[0] == name:
        print(_)
    
    


# In[ ]:




