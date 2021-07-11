#creating sets
set1={"cat","dog","elephant","horse","dog"}
set2={"dog","lion","cheetha"}

#adding an element
set1.add("tiger")
print(set1)

#returns a set contaning the difference
x=set1.difference(set2)
print(x)

#discarding an element from the set
set2.discard("lion")
print(set2)

#intersection of two sets
x1=set1.intersection(set2)
print(x1)

#checks whether two sets have a intersection or not
x2=set1.isdisjoint(set2)
print(x2)

#removing an element from the set
set1.remove("horse")
print(set1)

#returns a set with the symetric differences of two sets
x3=set1.symmetric_difference(set2)
print(x3)

#return a set containing the union of sets
x4=set1.union(set2)
print(x4)

#removing all the elements of the set
set2.clear()
print(set2)