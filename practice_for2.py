# Search for a number x in this tuple using loop:

# (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

nums=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=49
index=0
for el in nums:
    if(el==x):
        print("Number is found at index", index)
index=index+1    