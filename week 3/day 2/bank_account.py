class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def view_account(self):
        print('name:', self.owner)
        print('balance:£', self.balance)

    def add(self, amount):
        self.balance += amount
        print(self.balance)

    def remove(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(self.balance)
            return True
        else:
            print('Not enough funds to withdraw!')
            return False





def deposit(account):
    try:
        amount = float(input('Deposit:£'))
        if amount > 0:
            account.add(amount)
            print('Money added!')
            return
        else:
            print('Please enter a number above 0!')
            return
    except ValueError:
        print('Please enter a valid amount!')
        return


def withdraw(account):
    try:
        amount = float(input('Withdraw: £'))

        if amount <= 0:
            print('Please enter a valid withdrawal amount!')
            return

        if account.remove(amount):
            print('Money withdrawn!')

    except ValueError:
        print('Please enter a valid input!')



account = BankAccount("Matthew", 0)

while True:
    print('---- Bank Account ----')
    print('1. view account')
    print('2. deposit')
    print('3. withdraw')
    print('4. exit')
    choice = input('Choice: ')

    if choice == '1':
        account.view_account()
    elif choice == '2':
        deposit(account)
    elif choice == '3':
        withdraw(account)
    elif choice == '4':
        print('Have a good rest of your day!')
        break
    else:
        print('Please enter a valid input!')

