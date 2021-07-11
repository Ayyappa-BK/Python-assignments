#creating a dictionary
dict1={"brand":"Lamborghini","model":"Aventador","year":"2012"}

#returning the value of the specified keys and value
x=dict1.get("brand")
print(x)

#retuning the dictionary's key value pairs
x1=dict1.items()
print(x1)

#returning the keys
x2=dict1.keys()
print(x2)

#removing a specific element
dict1.pop("year")
print(dict1)

#returning a list of all the values in the dictionary
x3=dict1.values()
print(x3)

#removing all the elements from the dictionary
dict1.clear()
print(dict1)