with open('message.txt','w') as file:
    file.write('Hello from python!')

with open('message.txt', 'r') as file:
    contents = file.read()

print(contents)

with open('message.txt', 'r') as file:
    for line in file:
        print(line.strip())

with open('message.txt', 'a') as file:
    file.write('\nRoss')

with open('message.txt', 'r') as file:
    for line in file:
        print(line.strip())