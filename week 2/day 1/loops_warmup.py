numbers = [12, 5, 8, 21, 3, 17, 10]

for number in numbers:
    print(number)

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        continue
print(even_numbers)

total = 0

for number in numbers:
    total += number

print(total)

largest_number = numbers[0]

for number in numbers:
    if (number > largest_number):
        largest_number = number
    else:
        continue

print(largest_number)


smallest_number = numbers[0]
for number in numbers:
    if (number < smallest_number):
        smallest_number = number
    else:
        continue
print(smallest_number)

count = 0
total = 0

for number in numbers:
    total += number
    count += 1

average = total / count
print(average)