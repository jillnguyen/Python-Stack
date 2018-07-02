words = "It's thanksgiving day. It's my birthday, too"
words.find("day")
replacement = words.replace("day","month")
x = [2, 54, -2, 7, 12, 98]
min(x)
max(x)
y = []
z = ["hello", 2, 54, -2, 7, 12, 98, "world"]
y.append(z[0])
y.append(z[len(z)-1])
my_array = [19, 2, -8, 15, -21, 0, 98, 6, -55, 7]
my_array.sort()
new_arr1 = []
new_arr = [0]
half_length = len(my_array)/2
for i in range(0, half_length):
    new_arr1.append(my_array[i])
for i in range(0, half_length):
    new_arr.append(half_length + i)
new_arr[0] = new_arr1
print(words)
print(replacement)
print(min(x), max(x))
print(y)
print (new_arr)