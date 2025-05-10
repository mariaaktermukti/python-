# WAP to find the sum of first n numbers. (using for)
n=int(input("Enter number :"))
sum=0
for i in range(1,n+1):
    sum= sum+i
 
print("Sum is : ", sum)     