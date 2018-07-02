def make_dict(list1, list2):
    new_dict = {}
    if len(list1) > len(list2):
        for i in range (0, len(list1)):
            new_dict[list1[i]] = list2[i]
        return new_dict
    elif len(list1) < len(list2):
        for i in range (0, len(list1)):
            new_dict[list2[i]] = list1[i]
        return new_dict     
    else:
        for i in range (0, len(list1)):
            new_dict[list1[i]] = list2[i]
        return new_dict


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "me"]

my_dict = make_dict(name,favorite_animal)
print my_dict


