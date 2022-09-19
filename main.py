num1 = [1, 2, 3, 4, 5, 6]
num2 = [7, 8, 9, 10, 11, 12]


def median_result(
        array1: list, array2: list
) -> int:
    for item in range(len(array2)):
        array1.append(array2[item])
    if len(array1) % 2 == 0:
        median = (array1[len(array1)//2] + array1[(len(array1)//2) - 1])/2
        return median
    elif len(array1) % 2 != 0:
        array1.pop()
        median = array1[len(array1)//2+1]
        return median


print(len(num1+num2))
print(num1+num2)
print(median_result(num1, num2))