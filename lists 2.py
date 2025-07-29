#Adding and removing items from a list

fruits = ["apple", "banana", "cherry"]

fruits.append("kiwi")    #this is to add
print(fruits)

fruits.insert(1, "orange")  #to add something @ a specific position
print(fruits)


fruits.remove("kiwi") 
print(fruits) 

#SORT METHOD

fruits.sort(reverse=True)
print(fruits)