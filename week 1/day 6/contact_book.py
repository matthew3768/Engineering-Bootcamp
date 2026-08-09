contact_book = {}

def add_contact(contact_book):
    contact_name = input('Please enter the name of the contact: ')
    contact_phone = input('Please enter the phone number of the contact: ')
    contact_email = input('Please enter the email of the contact: ')

    new_contact_id = f'contact{len(contact_book) + 1}'

    contact_book[new_contact_id] = {
        'name': contact_name,
        'phone number': contact_phone,
        'email': contact_email
    }

    print('contact added')

def view_contacts(contact_book):
    for contact_id, contact_details in contact_book.items():
        print(f"ID: {contact_id}, || name: {contact_details['name']}, || phone: {contact_details['phone number']}, || email: {contact_details['email']}")

    print('--------------------')

def search_contact(contact_book):
    person = input('Name: ')

    for contact_id, contact_details in contact_book.items():
        if contact_details['name'].lower() == person.lower():
            print(contact_details)
            return

    print('Contact not found!')

def update_contact(contact_book):
    person = input('Person you wish to update: ')

    for contact_id, contact_details in contact_book.items():
        if contact_details['name'].lower() == person.lower():
            option = input('Please enter n to update name, p to update phone number or e to update email: ')
            if option.lower() == 'n':
                new_name = input('Please enter the new name of this contact: ')
                contact_details['name'] = new_name
                print('Name updated')
                return
            elif option.lower() == 'p':
                new_phone = input('Please enter the phone number of this contact: ')
                contact_details['phone number'] = new_phone
                print('Phone number updated')
                return
            elif option.lower() == 'e':
                new_email = input('Please enter the new email of this contact: ')
                contact_details['email'] = new_email
                print('Email updated')
                return
            else:
                print('Invalid input!')
                return

    print('Person not found!')

def delete_contact(contact_book):
    person = input('Plese enter the name you wish to delete: ')

    for contact_id, contact_details in contact_book.items():
        if contact_details['name'].lower() == person.lower():
            contact_book.pop(contact_id)
            print('Contact deleted')
            return
    print('Contact not found!')

while True:
    print('Press 1 to add a contact')
    print('Press 2 to view contacts')
    print('Press 3 to search fot a contact')
    print('Press 4 to update a contact')
    print('press 5 to delete a contact')
    print('press 6 to exit')
    choice = input('Which option do you want: ')

    if choice == '1':
        add_contact(contact_book)
    elif choice == '2':
        view_contacts(contact_book)
    elif choice == '3':
        search_contact(contact_book)
    elif choice == '4':
        update_contact(contact_book)
    elif choice == '5':
        delete_contact(contact_book)
    elif choice == '6':
        print('Have a good rest of your day!')
        break
    else:
        print('Invalid choice, try again!')
