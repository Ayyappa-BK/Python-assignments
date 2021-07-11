#creating the list
list1=["cat","dog","elephant","horse","dog"]
list2=["parrot","crow"]

#printing original list1
print(list1)

#using append
list1.append("monkey")
print(list1)  

#printing the count of a particular word
x=list1.count("dog")
print("The count of word dog is: ",x)

#extending list1 with list2
list1.extend(list2)
print(list1)

#printing the index of the particular word/element
print("The index of horse is: ",list1.index("horse"))

#inserting an element at specific position
list1.insert(3,"pigeon")
print(list1)

#poping the last element
list1.pop()
print(list1)

#removing an element
list2.remove("crow")
print(list2)

#reversing the list1
list1.reverse()
print(list1)

#sorting the list
list1.sort()
print(list1)

#clearing all the elements in the list1
list1.clear()
print(list1)