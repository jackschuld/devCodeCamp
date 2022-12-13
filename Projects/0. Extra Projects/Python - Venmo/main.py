from account import Account

jackschuld = Account('schuldjack@gmail.com', 'Jack Schuld')
parson = Account('parsondapup@gmail.com', 'Parson')

print(jackschuld.balance)
print(parson.balance)

jackschuld.transfer_money(parson, 10)

jackschuld.deposit(52)

print(jackschuld.balance)
print(parson.balance)

jackschuld.transfer_money(parson, 10)

print(jackschuld.balance)
print(parson.balance) 