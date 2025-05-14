# WAF to print the elements of a list in a single line. ( list is the parameter)

cities=["Dhaka","mym","barisal"]
heroes=["Thor","Iron man","Captain America"]


def print_len(list):
    print(len(list))

# print_len(cities)
# print_len(heroes) 

def print_list(list):
    for item in list:
        print(item, end=" ")
        
print_list(heroes) #Thor Iron man Captain America 
print( )  #print space
print_list(cities)  #Dhaka mym barisal       