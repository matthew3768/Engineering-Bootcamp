import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)

        return contacts

    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    
    name = input('name: ').strip()
    phone = input('phone: ').strip()
    email = input('email: ').strip()

    new_contact = {
        'name': name,
        'phone': phone,
        'email': email
    }

    contacts.append(new_contact)
    save_contacts(contacts)
    print('Contact saved!')


def view_contacts(contacts):
    if not contacts:
            print('No contacts found!')
            return

    for number, contact_details in enumerate(contacts, start=1):
        print(number,')','\n', 'name:', contact_details['name'], '\n', 'phone:', contact_details['phone'], '\n','email:', contact_details['email'])


def search_contacts(contacts):
    name = input('Enter contact name: ').strip()
    
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print('name:', contact['name'], '\n', 'phone:', contact['phone'], '\n', 'email:', contact['email'])
            return

    print('contact not found!')      

def delete_contact(contacts):
    name = input('Enter the name of the contact you want to delete: ')

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print('Contact deleted!')
            return

    print('Contact not found!')

contacts = load_contacts()

while True:
    print('---- CONTACT MANAGER ----')
    print('1. Add contact')
    print('2. View contact')
    print('3. search contact')
    print('4. Delete contact')
    print('5. Exit')
    choice = input('Please enter your choice: ')

    if choice == '1':
        add_contact(contacts)
    elif choice == '2':
        view_contacts(contacts)
    elif choice == '3':
        search_contacts(contacts)
    elif choice == '4':
        delete_contact(contacts)
    elif choice == '5':
        print('Have a good rest of your day!')
        break
    else:
        print('Please enter a valid number!')