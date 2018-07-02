my_dict = {
    "name" : "Jill",
    "age" : 26,
    "country of birth": "Vietnam",
    "favourite language": "Javascript",
    "favourite food": "BBQ",
    "pet": "Nem"
}

def reading_dict(the_dict):
    for k,v in the_dict.iteritems():
        myline = "My " + str(k) + " is " + str(v)
        print myline

reading_dict(my_dict)