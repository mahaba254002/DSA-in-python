import array,numpy as np

num = array.array("i", [56, 56, 78, 90])
print("Before appending: ", num)

num.append(806)
print("After appending", num)

print(num.buffer_info())  # returns address of array and length
print(num.count(56))  # returns how many times a number is repeated

x = array.array("i", [5, 5])
num.extend(x)  # extends the array by adding more at the end
print(num)

num.insert(0, 900)
print(num)

num.pop(2)  # Argument is index(item position)
num.remove(56)  # removes the first occurrence of an element
print(num)

numArray=np.array(["mango","Apple"])
print(numArray)
print(len(num))