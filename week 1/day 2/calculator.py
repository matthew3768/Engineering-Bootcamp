def addition(a, b):
        return a + b
def subtraction(a, b):
        return a - b
def multiplication(a, b):
        return a * b
def division(a, b):
        return a / b



print('Press 1 for addition')
print('press 2 for subtraction')
print('press 3 for multiplaction')
print('press 4 for division')

while True:

   choice = input('Please enter your choice of calcualtion.')

   if choice in ('1', '2', '3','4'):
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue 

    if choice == '1':
          print(num1, '+', num2, '=', addition(num1, num2))
    elif choice == '2':
          print(num1, '-', num2, '=', subtraction(num1, num2))
    elif choice == '3':
          print(num1, '*', num2, '=', multiplication(num1, num2))
    elif choice == '4':
          print(num1, '/', num2, '=', division(num1, num2))

    next_calculation = input('Want to do another calculation(yes/no)?')
    if next_calculation.lower == 'no':
          break
   else: 
        print('Invalid input ')
          
                 
        