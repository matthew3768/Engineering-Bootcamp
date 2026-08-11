first_name = input('Enter first name: ')
second_name = input('Enter second name: ')
date_of_birth = input('Enter year of birth: ')

first_name = first_name.capitalize()
second_name = second_name.lower()
date_of_birth = date_of_birth[-2:]

print(f'your password: {first_name}{second_name}{date_of_birth}')


