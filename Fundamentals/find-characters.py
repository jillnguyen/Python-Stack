word_list = ['hello','world','my','name','is','Anna']
char = 'o'
def find_char(my_list,char):
    new_list = []
    for x in my_list:
        for j in x:
            if j == char:
                new_list.append(x)
    print (new_list)
find_char(word_list, char)                 