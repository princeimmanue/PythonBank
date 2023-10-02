import balance
def Debosite():
    print("[$] Debosite Money >>")
    amount = float(input("[*]Amount :"))
    total_balance = amount + balance.wallet
    balance.wallet = total_balance
    print(f"[*] {amount} is Debosited to your wallet.")
    print(f'Balance is : {balance.wallet} ')
