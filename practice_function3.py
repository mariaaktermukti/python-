# WAF to find the factorial of n. (n is the parameter)

def cal_fact(n):
    fact=1
    for i in range(1,n+1):
       fact= fact *i
    print(fact)
    
cal_fact(int(input("Enter the value of n: ")))       
    