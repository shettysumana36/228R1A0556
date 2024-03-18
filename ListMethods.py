my_list=[1,2,3,4,]
'''
List methods:
1.sort()
2.clear()
3.append()
4.count()
5.extend()
6.insert()
7,index()
8.len()
9.remove()
10.pop()
11.reverse()
12.copy()
13.min()
14.max()
16.del()
'''
myList=[1,2,3,4,5,6]
myList.sort()
print(myList)
myList.append(99)
print(myList)
myList.extend([44,77,88])
print(myList)
#to count number of tyms the element is present
print(myList.count(4))
#insert 22 at index 1
myList.insert(1,22)
print(myList)
max=max(myList)
print(max)
min=min(myList)
print(min)
#deleting an element at index 2
del myList[2]
print(myList)
copyList = myList.copy()
print("Copied List= ", copyList)
copyList.reverse()
print("ReverseList= ", copyList)


