# ascending order
list=[9,1,3,4]
list.append(6)
print(list)
print(list.sort())
print(list)

#decending order
list=[9,1,3,4]
list.append(6)
print(list)
print(list.sort(reverse=True))
print(list)
list2=['a','r','p','f','z']
print(list2)         #['a', 'r', 'p', 'f', 'z']
print(list2.sort())  #None
print(list2)         #['a', 'f', 'p', 'r', 'z']
print(list2.sort(reverse=True))  #None
print(list2)    #['z', 'r', 'p', 'f', 'a']