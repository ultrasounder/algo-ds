class CreditCard:
    """ create a credit card instance

    The initial balance is zero

    customer the name of the customer 
    bank the name of the bank

    acnt the account identifier
    limit the credit limit

    """
    def __init__(self, name, bank, acnt, limit):

        self._name = name
        self._bank = bank
        self._acnt  = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._name
    
    def get_bank(self):
        return self._bank

    def get_acnt(self):
        return self._acnt
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance

    def charge(self, price):
        """charge given price to credit card assuming sufficient credit limit.
        Return True if card is charged, False if charge is unsuccesful.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, amnt):
        self._balance += amnt


cc = CreditCard("Ananth", "Chase", "5391 4546 0387 5309", 1000)

if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard('John Bowman', 'Wells Fargo', '5391 1046 5235 5783', 2500))
    wallet.append(CreditCard('John Bownman', 'California Federal', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowmna', 'California Finance', '5391 0375 9387 5309', 5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(val * 2)
        wallet[2].charge(val * 3)
    
    for c in range(3):
        print('Customer =', wallet[c]. get_customer)
        print('Bank =', wallet[c].get_bank)
        print('account=', wallet[c].get_acnt)
        print('balance=', wallet[c].get_balance)
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New Balance =', wallet[c].get_balance())
    
        print()

