def grades(the_scores):
    print ("Scores and Grades")
    for i in range (0, len(the_scores)):
        if 60 < the_scores[i] and the_scores[i] <= 69:
            print ("Score:", the_scores[i], "; Your grade is D")
        elif 70 < the_scores[i] and the_scores[i] <= 79:
            print ("Score:", the_scores[i], "; Your grade is C")
        elif 80 < the_scores[i] and the_scores[i] <= 89:
            print ("Score:", the_scores[i], "; Your grade is B")
        else:
            print ("Score:", the_scores[i], "; Your grade is A")

grades([67, 89, 83,72,69,93,68,86,80,99])
