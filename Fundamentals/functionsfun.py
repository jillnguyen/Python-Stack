# Odd/Even
def odd_even1to2000():
    for i in range (1,2001):
        if i%2 == 0:
            print ("Number is", i, ". This is an even number")
        if i%2 ==1:
            print ("Number is", i, ". This is an odd number")
odd_even1to2000()

#Multiply
def multiply(my_list,factor):
    new_list = []
    for i in range (0, len(my_list)):
        new_list.append(my_list[i] * factor)
    return new_list

a = [5, 4, 8 ,10, -5, 0] 
my_values = multiply(a,3)
print my_values

#Layered Multiply
def layered_multiplies(the_list,num):
    final_list = []
    for i in range (0, len(the_list)):
        temp_list = []
        times = the_list[i] * num
        for i in range (0, times):
            temp_list.append(1)
        final_list.append(temp_list)
    return final_list

here = layered_multiplies([2, 4, 3, 9], 2)
print here      

