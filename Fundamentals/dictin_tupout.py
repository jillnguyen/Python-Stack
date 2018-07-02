my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dictin_tupout(dict):
    my_list = []
    for k in dict:
        my_tuple = ()
        my_tuple = my_tuple + (k,)
        my_tuple = my_tuple + (dict[k],)
        my_list.append(my_tuple)
    print my_list

dictin_tupout(my_dict)        

