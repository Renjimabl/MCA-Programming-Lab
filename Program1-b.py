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
