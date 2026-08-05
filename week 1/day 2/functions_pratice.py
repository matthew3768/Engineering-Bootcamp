def calculate_area(length, width):
    return length * width

print(calculate_area(5,7))

def is_even_number(number):
    if (number % 2 == 0):
        return True
    else:
        return False
print(is_even_number(5))
print(is_even_number(8))

def larger_number(a, b):
    if (a > b):
        return a
    else:
        return b

print(larger_number(12,6))
print(larger_number(3,10))

def print_uppercase(txt):
    upper_case = txt.upper()
    return upper_case

print(print_uppercase("How are we today?"))

def find_average(numbers):
    total = 0
    i = 0
    for number in numbers:
        total = number + total
        i += 1
    average = total // i
    return average

list_of_numbers = [3,5,7,9,10,26]
print(find_average(list_of_numbers))

def password_valid(password):
  min_length = 8
  has_number = any(char.isdigit for char in password)
  is_long_enough = len(password) > min_length

  if is_long_enough and has_number:
      return True
  else:
      return False

print(password_valid('HARRY3768'))
print(password_valid('bob'))





