class Payment():
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print('Processing payment....')

    def display_info(self):
        print('amount: £', self.amount)


class CardPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def process_payment(self):
        print('Processing £', self.amount,'card payment')

    def display_info(self):
         print('Payment type: Card')
         super().display_info()


class PayPalPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def process_payment(self):
        print('Processing £', self.amount, 'PayPal payment')

    def display_info(self):
        print('Payment type: PayPal')
        super().display_info()
    

class BankTransfer(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def process_payment(self):
        print('processing £', self.amount, 'Bank transfer')

    def display_info(self):
        print('Payment type: Bank transfer')
        super().display_info()


payments = []

def add_card_payment(payments):
    try:
        amount = float(input('amount: £'))
        if amount <= 0:
            print('Amount cannot be negative!')
            return

    except ValueError:
        print('Please enter correct pay format!')
        return

    new_payment = CardPayment(amount)
    payments.append(new_payment)
    print('Transaction processed!')

def add_pay_pal_payment(payments):
    try:
        amount = float(input('amount: £'))
        if amount <= 0:
            print('Amount cannot be negative!')
            return
    
    except ValueError:
        print('Please enter correct pay format!')
        return
    
    new_payment = PayPalPayment(amount)
    payments.append(new_payment)
    print('Transaction processed!')

def add_bank_transfer(payments):
    try:
        amount = float(input('amount: £'))
        if amount <= 0:
            print('Amount cannot be negative!')
            return
    
    except ValueError:
        print('Please enter correct pay format!')
        return
    
    new_payment = BankTransfer(amount)
    payments.append(new_payment)
    print('Transaction processed!')

def view_payments(payments):
    for payment_number, payment in enumerate(payments, start=1):
        print(payment_number, ')')
        payment.display_info()
        

def process_payments(payments):
    for payment in payments:
        payment.process_payment()


while True:
    print('---- Payment system ----')
    print('1. Add card payment')
    print('2. Add paypal payment')
    print('3. Add bank transfer')
    print('4. View payments')
    print('5. Process payments')
    print('6. Exit')
    choice = input('choice:')

    if choice == '1':
        add_card_payment(payments)
    elif choice == '2':
        add_pay_pal_payment(payments)
    elif choice == '3':
        add_bank_transfer(payments)
    elif choice == '4':
        view_payments(payments)
    elif choice == '5':
        process_payments(payments)
    elif choice == '6':
        print('Have a good rest of your day!')
        break
    else:
        print('Please enter a valid input!')
