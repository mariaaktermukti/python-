#set.add(el)-->add an elements
collection= set()
collection.add(1)
collection.add(2)
collection.add(2) #ignore duplicate elements

print(collection)  #{1, 2}
# collection.remove(2)
# print(collection) #{1}

collection.add("Mukti")
collection.add((1,2,3,4))
print(collection)