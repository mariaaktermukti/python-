#.get("key")--> returns the key according to value
student={
    "name":"Maria Mukti",
    "Subjects":{   #nested
        "phy": 96,
        "chem": 98,
        "math": 94,
        "Bio": 99
    }
}
print(student["name"])  #Maria Mukti
print(student.get("name"))  #Maria Mukti
