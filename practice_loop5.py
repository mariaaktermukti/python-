# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

nums= (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=49
i=0
while i< len(nums):
    if(nums[i]== x):
        print("Found at index ",i)
    else:
        print("Finding...")    
    i=i+1    
    