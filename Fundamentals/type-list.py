list1 = ["my home", 19, -5, "is", 2, "old"]
list2 = [2,3,1,7,4,12]
list3 = ["Coding", "is", "fun"]

def list_type(arr):
    my_sum = 0
    string = ""
    counter_str = 0
    counter_num = 0
    for i in range (0, len(arr)):
        if isinstance(arr[i], int) or isinstance(arr[i], float):
            my_sum += arr[i]
            counter_num += 1
        if isinstance(arr[i], str):
            string += arr[i]
            counter_str += 1
    if counter_num != 0 and counter_str !=0:
        print("This is a mixed list")
        print("String is: ", string)
        print("Sum is:", my_sum)
    elif counter_num == 0:
        print("This list is of string type")
        print("String:", string)
    else:
        print("This list is of number type")
        print("Sum:", my_sum)
list_type(list1)
list_type(list2)
list_type(list3)               


            