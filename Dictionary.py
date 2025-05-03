info={
    "key" : "Value",  #1.Key can be anything, like int, float, char..so no.. 2. they are unordered, mutable(changeable), don't allow duplicate keys
    "Name": "Mukti",
    "Learning": "Python",
    "Age" : 22,
    "is_adult" : True,
    "marks": 98,
    "Subject":["Python","C","C++","Java"],
    "topics" :("dictionary","Set")
}
print(type(info))
print(info)
print(info["Age"])

info["name"]="Maria"
print(info)

null_dict={}
print(null_dict)
#i can also add something in the null dict
null_dict["name"]="Shifat"
print(null_dict)