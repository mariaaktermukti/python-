def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)    


# output:
#     5
#     4
#     3
#     2
#     1