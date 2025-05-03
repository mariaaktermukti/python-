student={
    "name":"Maria Mukti",
    "Subjects":{   #nested
        "phy": 96,
        "chem": 98,
        "math": 94,
        "Bio": 99
    }
}
print(student) # {'name': 'Maria Mukti', 'Subjects': {'phy': 96, 'chem': 98, 'math': 94, 'Bio': 99}}
print(student["Subjects"]) #{'phy': 96, 'chem': 98, 'math': 94, 'Bio': 99}
print(student["Subjects"] ["math"]) #94