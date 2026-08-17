def name_check(name):
    if name.strip() == "":
        print("Name cannot be empty!")
        return False
    else:
        return True


def age_check(age):
    if age >= 16 and age <= 100:
        return True
    else:
        print("Age must be between 16 and 100.")
        return False


def check_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        print('Email does not fit the required structure!')
        return False

while True:
    name = input("Please enter your name: ")

    if name_check(name):
        break

print(f"Your name is {name}")


def check_password(password):
    if len(password) < 8:
            print('password must contain at lest 8 characters')
            return False
    if not any(char.isupper() for char in password):
            print('Password must contain a capital letter!')
            return False
    if not any(char.islower() for char in password):
            print('Password must contain a lowercase letter!')
            return False
    if not any(char.isdigit() for char in password):
            print('Password must contain a number!')
            return False

    else:
         return True

while True:
    try:
        age = int(input("Please enter your age: "))

        if age_check(age):
            break

    except ValueError:
        print("Please enter a valid number.")

print(f"You are {age} years old.")

while True:
    email = input('Please enter your email: ')

    if check_email(email):
        break

print(f'your email is: {email}')

while True:
    password = input('Please enter a password: ')

    if check_password(password):
         break


print('Password saved!')

user_details = {
     'name': name,
     'age': age,
     'email': email,
}

def display_details(user_details):
     print(f'Name: {user_details.get('name')}')
     print(f'Age: {user_details.get('age')}')
     print(f'Email: {user_details.get('email')}')

display_details(user_details)

