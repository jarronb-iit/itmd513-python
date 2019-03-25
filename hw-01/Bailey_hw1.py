# Stock Transaction Program (Homework 1)
# Name: Jarron Bailey

shares_purchased = 2000
purchased_price = 40.00
selling_price = 42.75
commission_percentage = .01  # Net should be higher since commission is lower

# Total amount of money Joe paid for the stock
total_purchased_price = purchased_price * shares_purchased
print('Total amount of money Joe paid for the stock:  %.2f' %
      total_purchased_price)

# The amount of comission Joe paid his broker when he bought the stock
commission1 = total_purchased_price * commission_percentage
print('The amount of comission Joe paid his broker when he bought the stock:  %.2f' % commission1)

# The amount for which Joe sold the stock
total_selling_price = shares_purchased * selling_price
print('The amount for which Joe sold the stock:  %.2f' % total_selling_price)

# The amount of comission Joe paid his broker when he sold the stock
commission2 = total_selling_price * commission_percentage
print('The amount of comission Joe paid his broker when he bought the stock:  %.2f' % commission2)

# The amount Joe had left after broker was paid
total_comission = commission1 + commission2
net_gains = total_selling_price - total_purchased_price - total_comission
print('Joe net gains:  %.2f' % net_gains)
