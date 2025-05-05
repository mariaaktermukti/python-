# .items()--> returns all the (keys,val) pairs as tuples
student={
    "name":"Maria Mukti",
    "Subjects":{   #nested
        "phy": 96,
        "chem": 98,
        "math": 94,
        "Bio": 99
    }
}
pairs=list(student.items())
print(pairs[0])  #('name', 'Maria Mukti')
print(student.items())  
print(list(student.items()))