array = []
for x in range(2, 10):
    array.append(x)

print(array)

index = 0
while index < len(array):
    for x in range(index + 1, len(array)):
        ##print("Index:" + str(array[index]))
        ##print("x:" + str(array[x]))
        if array[x] % array[index] == 0:
            array.remove(array[x])

    index = index + 1

for x in array:
    print(x)
