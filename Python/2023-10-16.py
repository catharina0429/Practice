print(7/4)
print(7%4) # calculating reminder

"""
Currency Exchange
"""
def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    
    this function should return the value of the exchanged currency.
    Note: If your currency is USD and you want to exchange USD for EUR with an exchange rate of 1.20, then 1.20 USD == 1 EUR
    """

    return budget / exchange_rate

print(exchange_money(127.5, 1.2))

def get_change(budget, exchanging_value):
    """
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    
    this function should return the amount of money that is left from the budget
    """

    return budget - exchanging_value 

print(get_change(127.5, 120))

def get_value_of_bills(denomination, number_of_bills):
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills
print(get_value_of_bills(5, 128))

def get_number_of_bills(budget, denomination):
    """
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination

print(get_number_of_bills(127.5, 5))

def get_leftover_of_bills(budget, denomination):
    """
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    return budget % denomination
print(get_leftover_of_bills(127.5, 20))

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.

    This function should return the maximum value of the new currency after calculating the exchange rate plus the spread. 
    Remember that the currency denomination is a whole number, and cannot be sub-divided.
    """
    actual_rate = exchange_rate * (1 + spread / 100)
    total_value = exchange_money(budget, actual_rate)
    bill_count = get_number_of_bills(total_value, denomination)
    return get_value_of_bills(denomination, bill_count)
print(exchangeable_value(127.25, 1.20, 10, 5))
print(exchangeable_value(1500, 0.84, 25, 40))