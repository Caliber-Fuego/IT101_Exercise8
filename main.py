data = [5, 3, 7]

# 1. Assume that the variable data refers to the list [5, 3, 7]. Write the values of the following expressions:

print(data[2])
print(data[-1])
print(len(data))
print(0 in data)
print(data + [2, 10, 5])
print(tuple(data))

print("\n")
# 2. Assume that the variable data refers to the list [5, 3, 7]. Write the expressions that perform the following tasks:

data[0] = -data[0]
print(data)

data.append(10)
print(data)

data.insert(2, 22)
print(data)

data.pop(1)
print(data)

data.sort()
print(data)

