

def get_valid_number(prompt):
    while True:
        try:
            age = int(input(prompt))
            print(f"You are {age} years old.")
            break
        except ValueError:
            print("Please enter a valid number.")


get_valid_number('Please enter your age: ')