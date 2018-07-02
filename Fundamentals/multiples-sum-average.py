#Print odd numbers from 1 to 1000
def print_odd():
    for i in range(1, 1000, 2):
        print(i)
#Print multiples of 5 from 5 to 1000000
def print_multiples_5():
    for i in range(5, 1000000, 5):
        print(i)
#Print sum value
a = [1, 2, 5, 10, 255,3]
def find_sum(arr):
    sum = 0
    for x in arr:
        sum += x  
    return sum

#Print average
def find_average(arr):
    the_sum = find_sum(arr)
    return the_sum/len(arr)

pring_odd()
print_multiples_5()
my_sum = find_sum(a)
my_average = find_average(a)
print(my_sum, my_average)    

