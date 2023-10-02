import balance

def tranfermoney():
    accno = input("[*] Acc no :")
    Amount = float(input("Amount :"))
    update_balance  = balance.wallet - Amount
    balance.wallet = update_balance
    print(f'[*] {Amount} was transfer to {accno}')
    print(f'[*] Balance is : {balance.wallet}' )

