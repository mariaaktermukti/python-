#.update(newDict)-->insert the specified items to the dictionary
student={
    "name":"Maria Mukti",
    "Subjects":{   #nested
        "phy": 96,
        "chem": 98,
        "math": 94,
        "Bio": 99
    }
}

new_dict= student.update({"city":"Dhaka", "age": 22})
new_dict= student.update({"name":"shifat", "age": 23})
print(student)
