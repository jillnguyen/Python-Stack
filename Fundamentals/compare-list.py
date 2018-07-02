def compare_list(list1, list2):
    if len(list1) != len(list2):
        print(list1, list2, "Two list are not the same")
    else:
        my_comparison = True
        idx = len(list1)
        for i in range (0, idx):
            if not list1[i] == list2[i]:
                my_comparison = False
        if my_comparison == False:
            print(list1, list2, "Two lists are of similar length but not the same")
        else:
            print(list1, list2,"Two list are identical")
a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = ["hello", "how", 1, 2, 3]
d = [1,2,3]
compare_list(a,b)
compare_list(a,c)
compare_list(a,d)                              