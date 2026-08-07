number = int(input('Please enter the number of the multiplication table you want: '))
count = 1

for i in range(1,13):
    output = count * number
    print(count, '*', number, '=', output)
    count += 1

user_password = 'python123'

guess = input('Please enter your guess for the password: ')

while guess != user_password:
    guess = input('Wrong, please enter your guess for the password: ')
print('Password correct')
       
        