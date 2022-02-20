#!/usr/bin/env python
# coding: utf-8

# Write a python program to find the factorial of a number

# In[31]:


num = int(input("Enter a number: "))
f = 1

if num > 0:
   for i in range(1,num+1 ):  # to get from 1 upto input numbers in range and +1 as to take same input number
       f = f*i                # start with 1
   print("The factorial of",num,"is",f)
elif num == 0:
   print("The factorial of 0 is 0") # to avoid 1 output
else:
    print("Invalid  data")


# Write a python program to find whether a number is prime or composite

# In[60]:


num = int(input("Enter a number: "))
d=2
if num < 0:
   print("factorial does not exist for negative numbers")
elif num == 0:
    print("Zero is neither prime nor composite")
elif (num % i) == 0:
    print('It is Composite Number')
else:
    print('It is Prime Number')
    


# Write a python program to check whether a given string is palindrome or not

# In[64]:


Str = input("Please enter your own String : ")

if(Str == Str[:: - 1]):
   print("This is Palindrome word")
else:
   print("This is Not a Palindrome word")


# Write a Python program to get the third side of right-angled triangle from two given sides.
# 

# In[11]:


def pythagoras(opposite_side,adjacent_side,hypotenuse): # took google help
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5)) # formula will be same for opposite_side and adjacent_side
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))

    
print(pythagoras(3,4,'x'))


# Write a python program to print the frequency of each of the characters present in a given string.

# In[13]:


# Python3 code to demonstrate
# each occurrence frequency using
# naive method

# initializing string
test_str = "GeeksforGeeks"   # took google helps

# using naive method to get count
# of each element in string
all_freq = {}

for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1

# printing result
print ("Count of all characters in GeeksforGeeks is :\n "
										+ str(all_freq))


# In[ ]:




