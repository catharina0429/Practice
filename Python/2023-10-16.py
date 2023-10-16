print(7/4)
print(7%4) # calculating reminder

"""
exchange
"""
def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    
    this function should return the value of the exchanged currency.
    Note: If your currency is USD and you want to exchange USD for EUR with an exchange rate of 1.20, then 1.20 USD == 1 EUR
    """

    return budget/exchange_rate

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
