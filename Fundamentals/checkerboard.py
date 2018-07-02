def checkboard(row, column):
    my_string = ""
    for x in range (0,row):
        if x % 2 == 0:
            for idx in range (0,column):
                if idx % 2 == 0:
                    my_string += "*"
                else:
                    my_string += " "
            print(my_string)
            my_string = "" 
        else:
            for idx in range (0,column):
                if idx % 2 == 1:
                    my_string += "*"
                else:
                    my_string += " "
            print(my_string)
            my_string = "" 
checkboard(7,18)