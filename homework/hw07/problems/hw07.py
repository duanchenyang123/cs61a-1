class Fib:
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    """
    def __init__(self):
        self.value = 0
        self.next_value = 1

    def next(self):
        b = Fib()
        b.value = self.next_value
        b.next_value = b.value + self.value
        return b

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, item, cost):
        self.item = item
        self.cost = cost
        self.stock = 0
        self.amount_deposited = 0

    def restock(self, amount):
        self.stock += amount
        return 'Current {} stock: {}'.format(self.item, self.stock)

    def deposit(self, amount):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${}.'.format(amount)
        self.amount_deposited += amount
        return 'Current balance: ${}'.format(self.amount_deposited)

    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        elif self.amount_deposited < self.cost:
            return 'You must deposit ${} more.'.format(self.cost - self.amount_deposited)
        elif self.amount_deposited > self.cost:
            balance = self.amount_deposited - self.cost
            self.amount_deposited = 0
            self.stock -= 1
            return 'Here is your {} and ${} change.'.format(self.item, balance)
        else:
            self.amount_deposited = 0
            self.stock -= 1
            return 'Here is your {}.'.format(self.item)





class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> double_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> double_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        
        new_message = message[7:]

        if not hasattr(self.obj, new_message):
            return 'Thanks for asking, but I know not how to {}.'.format(new_message)
        elif isinstance(self.obj, MissManners):
            new_message = args[0][7:]
            if hasattr(self.obj.obj, new_message):
                return getattr(self.obj.obj, new_message)(args[1])
        else:
            return getattr(self.obj, new_message)(*args)







