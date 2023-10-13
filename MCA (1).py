#!/usr/bin/env python
# coding: utf-8

# In[3]:


r = int(input("enter the radius:"))
area = 3.14*r*r
print("area of the circle=",area)


# In[1]:


a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))
c = int(input("enter 3rd number:"))
if(a>b and a>c):
    print("a is greater")
elif(b>c and b>a):
    print("b is greater")
else:
    print("c is greater")
    


# In[4]:


n = int(input("enter a number:"))
temp = str(n)
nn = temp+temp
nnn = temp+temp+temp
sum = n+int(nn)+int(nnn)
print("The value is",sum)


# In[9]:


list1 = []
n = int(input("enter a number:"))
for i in range(0,n):
    a = int(input("enter the elements: "))
    if(a>=100):
        list1.append("over")
    else:
        list1.append(a)
print(list1)


# In[20]:


l1 = [1,2,3,4]
l2 = [3,4,5]
a = len(l1)
b = len(l2)
if(a==b):
    print("The list are same length")
else:
    print("The list are not same length")
sum1 = 0
sum2 = 0
for i in l1:
    sum1 = sum1+i
for j in l2:
    sum2 = sum2+j
if(sum1 == sum2):
    print("The list are same in sum values")
else:
     print("The list are not same in sum values")
count = 0
for i in l1:
    for j in l2:
        if(i==j):
            count=count+1
            print("same value in lists are",i)
if(count==0):
    print("No same elements in both list")
    


# In[6]:


a = int(input("enter first value:"))
b = int(input("enter second value:"))
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
g = gcd(a,b)
print("gcd:",g)


# In[ ]:


list1 = []
n = int(input("enter a range"))
for i in range(0,n):
    

