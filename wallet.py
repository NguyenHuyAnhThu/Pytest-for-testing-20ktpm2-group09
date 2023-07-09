class InsufficientAmount(Exception):
    pass


class NegativeMoney(Exception):
    pass


error = "Money shouldn't be negative"


class Wallet(object):
    def __init__(self, initial_amount=0):
        if initial_amount < 0:
            raise NegativeMoney(error)
        else:
            self.balance = initial_amount

    def spend_cash(self, amount):
        if amount < 0:
            raise NegativeMoney(error)
        else:
            if self.balance < amount:
                raise InsufficientAmount("Not enough available to spend {}".format(amount))
            else:
                self.balance -= amount

    def add_cash(self, amount):
        if amount < 0:
            raise NegativeMoney(error)
        else:
            self.balance += amount
