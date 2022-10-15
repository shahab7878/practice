#!/usr/bin/env python
# coding: utf-8

# # 1. Basic Calculator
# > 1. complete following functions and use them in the main function.\
# >> 1. add(x, y)
# >> 2. subtract(x, y)
# >> 3. multiply(x, y)
# >> 4. divide(x, y)
# 
# 
# Example of output:
# > Select an operator:
# > 1.Add
# > 2.Subtract
# > 3.Multiply
# > 4.Divide
# > Enter your choice(1/23/4): 3
# > Enter first number: 10
# > Enter second number: 5
# > 10.0 * 5.0 = 50.0
# > Leave the program?(y/n): n
# 

# In[ ]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

if __name__ == '__main__':

    while True:
        print('Select an operator:')
        print('1.Add')
        print('2.Subtract')
        print('3.Multiply')
        print('4.Divide')

        choice = input('Enter your choice(1/2/3/4): ')
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))

        if choice == '1':
            print(num1, '+', num2, '=', add(num1, num2))
        elif choice == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))
        elif choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))
        elif choice == '4':
            print(num1, '/', num2, '=', divide(num1, num2))
        else:
            print('Invalid input')

        leave = input('Leave the program?(y/n): ')
        if leave == 'y':
            break


# # 2. Mean Median and Mode
# > complete following functions and use them in the main function.
# >> 1. mean(numbers)
# >> 2. median(numbers)
# >> 3. mode(numbers)

# In[ ]:


# Mean
def mean(numbers):
    return sum(numbers) / len(numbers)



# Median
def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        m1 = numbers[len(numbers) // 2]
        m2 = numbers[len(numbers) // 2 - 1]
        return (m1 + m2) / 2
    else:
        return numbers[int(len(numbers) // 2)]



# Mode
def mode(numbers):
    frequency = {}
    for num in numbers:
        frequency.setdefault(num, 0)
        frequency[num]+=1

    frequent = max(frequency.values()) # find the max frequency
    for key, value in frequency.items():
        if value == frequent:
            mode = key

            return mode



if __name__ == '__main__':
    list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

    print("Mean:", mean(list1))
    print("Median:", median(list1))
    print("Mode:", mode(list1))


# # 3. Age Calculator
# > you need two dates:
# >> 1. birth date (ask user for input)
# >> 2. current date
# 
# complete following function and use it in the main function.
# > age_calculator(birth_date, current_date)

# In[ ]:


import datetime

def age_calculator(y, m, d):

    today = datetime.datetime.now().date()
    date_of_birth = datetime.date(y, m, d)
    age = int((today - date_of_birth).days / 365.25)

    return age

if __name__ == '__main__':
    print("Enter your birth date:")
    y = int(input("Year: "))
    m = int(input("Month: "))
    d = int(input("Day: "))

    print("Your age is:", age_calculator(y, m, d))


# # 4. Write a program that computes the net amount of a bank account based a transaction log from console input.
# > The transaction log format is shown as following:
# >> D 100
# >> W 200
# 
# **(D means deposit while W means withdrawal.)**
# 
# </br>
# 
# Suppose the following input is supplied to the program:
# >> D 300
# >> D 300
# >> W 200
# >> D 100
# >> resault : 500

# In[ ]:


def compute_net_amount(transaction_log):
    net_amount = 0
    for line in transaction_log:
        if line[0] == 'D':
            net_amount += int(line[1:])
        else:
            net_amount -= int(line[1:])

    return net_amount


if __name__ == '__main__':
    transaction_log = []
    while True:
        s = input()
        if not s:
            break
        transaction_log.append(s)

    print(f"resault : {compute_net_amount(transaction_log)}")


# In[ ]:


netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print(f"resault : {netAmount}")


# # 5. Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

# In[ ]:


import random

def random_even_number(from_, to):
    return random.choice([i for i in range(from_, to) if i % 2 == 0])

if __name__ == '__main__':
    print(random_even_number(0, 10))
    print(random_even_number(0, 10))
    print(random_even_number(0, 10))
    print(random_even_number(0, 10))


# # 6. Please write a program to shuffle and print the list [3,6,7,8].
# > (use random module.)

# In[4]:


from random import shuffle

if __name__ == '__main__':
    l = [3, 6, 7, 8]
    shuffle(l)
    print(l)


# # 7. lease write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
# > (use list comprehension to delete a bunch of element from a list.)

# In[5]:


if __name__ == '__main__':
    l = [5, 6, 77, 45, 22, 12, 24]
    l = [i for i in l if i % 2 != 0]
    print(l)


# # 8. With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
# > (use set)

# In[6]:


if __name__ == '__main__':
    l1 = [1, 3, 6, 78, 35, 55]
    l2 = [12, 24, 35, 24, 88, 120, 155]
    set1 = set(l1)
    set2 = set(l2)


    #set1 &= set2
    #list1 = list(set1)
    set3 = set1.intersection(set2)
    list3 = list(set3)
    print(l1)
    print(l2)
    print(f"intersection of l1 and l2 is {list3}")


# # 9. Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

# In[9]:


if __name__ == '__main__':
    l = [random.randint(100, 200) for i in range(5)]
    print(l)

