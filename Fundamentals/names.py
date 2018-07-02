students = [
    {"firstname": "Jill", "lastname": "Nguyen"},
    {"firstname": "Jeff", "lastname": "Ahn"},
    {"firstname": "Martin", "lastname": "Velasquez"},
    {"firstname": "Kevin", "lastname": "Kim"}
]

def print_names(stud_name):
    for i in range (0, len(stud_name)):
        full_name = ""
        for k in stud_name[i]:
            full_name = stud_name[i]["firstname"] + " " + stud_name[i]["lastname"]
        print full_name

print_names(students)

users = {
 'Students': [
     {'firstname':  'Jill', 'lastname' : 'Nguyen'},
     {'firstname' : 'Andre', 'lastname' : 'Loyola'},
     {'firstname' : 'Zoel', 'lastname' : 'Nguyen'},
     {'firstname' : 'Justin', 'lastname' : 'Tong'}
  ],
 'Instructors': [
     {'firstname' : 'Pattrick', 'lastname' : 'Choi'},
     {'firstname' : 'Eduardo', 'lastname' : 'Baik'}
  ]
 }

def user_data(my_class):
    for element in my_class:
        print element
        for i in range (0, len(my_class[element])):
            full_name = ""
            idx = i + 1
            full_name = str(idx) + " - " + my_class[element][i]["firstname"] + " " + my_class[element][i]["lastname"] + " - " + str(len(my_class[element][i]["firstname"])+len(my_class[element][i]["lastname"]))
            print full_name

user_data(users)