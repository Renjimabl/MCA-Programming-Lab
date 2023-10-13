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
