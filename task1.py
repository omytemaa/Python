numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
number_of_elements = len(numbers)
index = numbers.index(None)
numbers[index] = 0
sum_of_elements = sum(numbers)
numbers[index] = sum_of_elements/number_of_elements
print("Измененный список:",numbers)

