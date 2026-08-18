with open('names.txt', 'a') as file:
    name = input('Please enter your name: ')
    file.write(f'\n {name}')

with open('names.txt', 'r') as file:
    for lines in file:
        print(lines.strip())