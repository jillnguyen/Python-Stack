def draw_stars1(arr):
    for i in range (0,len(arr)):
        this_line =""
        for j in range (0, arr[i]):
            this_line += "*"
        print this_line

draw_stars1([2,4,7,1,9,5])

def draw_stars2(arr):
    for i in range (0,len(arr)):
        this_line =""
        if isinstance (arr[i], int):
            for j in range (0, arr[i]):
                this_line += "*"
            print this_line
        if isinstance (arr[i], str):
            letter = arr[i][0].lower()
            for j in range (0, len(arr[i])):
                this_line += letter
            print this_line

draw_stars2([2,7,"Jill", 9, "Zoel", "Chrissy", 3])            