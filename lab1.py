numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

total = 0
for num in numbers:
    if num is not None:
        total += num
avg = total / len(numbers)

i = 0
while i < len(numbers):
    if numbers[i] is None:
        numbers[i] = avg
        break
    i += 1
print(f'Измененный список: {numbers}')