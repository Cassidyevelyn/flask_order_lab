class Order():

    def __init__(self, customer_name, order_date, quantity):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
    
order1 = Order("Alabaster", "02/03/2023", 1)
order2 = Order("Brimstone", "02/03/2022", 1)
order3 = Order("Cosmo", "02/03/2021", 1)
order4 = Order("Morpho", "02/03/2020", 1)
order5 = Order("Greyling", "02/03/2019", 1)
order6 = Order("Yara", "02/03/2018", 1)

print(order1.order_date)
print(order2.order_date)
print(order4.customer_name)

