sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
def filter_type(value):
    if type(value)==int:
        if value > 100:
            print(value, "is a big number")
        else:
            print(value, "is a small number")
    if type(value)==str:
        if len(value)>50:
            print(value, "is a long sentence")
        else:
            print(value, "is a short sentence")
    if type(value)==list:
        if len(value)>10:
            print(value, "is a big list!")
        else:
            print(value, "is a short list")
filter_type(sI)
filter_type(mI)
filter_type(bI)
filter_type(eI)
filter_type(spI)
filter_type(sS)
filter_type(mS)
filter_type(bS)
filter_type(eS)
filter_type(aL)
filter_type(mL)
filter_type(lL)
filter_type(eL)
filter_type(spL)

