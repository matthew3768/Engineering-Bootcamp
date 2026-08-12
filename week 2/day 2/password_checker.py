while True:
        print('Password must contain 8 or more letters')
        print('Password must contain an uppercase and lowercase letter')
        print('Password must contain a number')
        password = input('Please enter a password: ')

        password_valid = True

        if len(password) < 8:
                print('password must contain at lest 8 characters')
                Password_valid = False
        if not any(char.isupper() for char in password):
                print('Password must contain a capital letter!')
                Password_valid = False
        if not any(char.islower() for char in password):
                print('Password must contain a lowercase letter!')
                Password_valid = False
        if not any(char.isdigit() for char in password):
                print('Password must contain a number!')
                Password_valid = False

        if password_valid == True:
                print('Password Valid!')
                break
        else:
                print('Password Invalid')


        
