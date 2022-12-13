class Account:
    
    def __init__(self, email, name, balance=0):
        self.email = email
        self.name = name
        self.balance = balance

    # Remove money from user's balance and add exact amount into other user's balance
    def transfer_money(self, to_account, amount):
        if self.balance < amount:
            print('Amount exceeds balance - Transfering amount must be less than amount in account balance.')
        else:
            self.balance -= amount
            to_account.balance += amount
            print(f'Successfully transfered ${amount} from your account to {to_account.name}\'s!')
    
    # Add money to account balance
    def deposit(self, amount):
        self.balance += amount
        print(f'Balance is now ${self.balance}')
    
