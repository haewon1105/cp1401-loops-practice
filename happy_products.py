"""
[All together now]
DISCOUNT THRESHOLD=5
DISCOUNT PERCENTAGE=10
DISCOUNT RATE=1-(DISCOUNT_PERCENTAGE/100)
MIN PRODUCTS=0
MIN PRICE=0
print 'Menu: '
print '(I)nstructions'
print '(C)alculate'
print '(Q)uit'
choice=input('Choice: ').lower()
while choice!='q'
    if choice=='i'
        print 'Enter the number of products you want to buy and your chosen price. '
        print f"If you buy {MIN_PRODUCTS}-{DISCOUNT_THRESHOLD} items, they're full price, over {DISCOUNT_THRESHOLD} items and each one is {DISCOUNT_PERCENTAGE}% off!"
    elif choice=='c'
        number of products=int(input('Number of products: '))
        while number_of_products<MIN_PRODUCTS
            print 'Invalid input'
            number of products=int(input('Number of products: '))
        price=float(input('Price: '))
        while price<=MIN_PRICE
            print 'Invalid input'
            price=float(input('Price:'))
        if number of products>DISCOUNT THRESHOLD
            price *= DISCOUNT_RATE
        total price = number of products * price
        print f'{number_of_products} x ${price:.2f} products = ${total_price:.2f}'
    else
        print 'Invalid choice'
    print 'Menu:'
    print '(I)nstructions'
    print '(C)alculate'
    print '(Q)uit'
    choice = input('Choice: ').lower()
print 'Farewell'
"""
DISCOUNT_THRESHOLD=5
DISCOUNT_PERCENTAGE=10
DISCOUNT_RATE=1-(DISCOUNT_PERCENTAGE/100) #10% discount-> 0.9 multiplier
MIN_PRODUCTS=0
MIN_PRICE=0
print('Menu: ')
print('(I)nstructions')
print('(C)alculate')
print('(Q)uit')
choice=input('Choice: ').lower()
while choice!='q':
    if choice=='i':
        print('Enter the number of products you want to buy and your chosen price. ')
        print(f"If you buy {MIN_PRODUCTS}-{DISCOUNT_THRESHOLD} items, they're full price, over {DISCOUNT_THRESHOLD} items and each one is {DISCOUNT_PERCENTAGE}% off!")
    elif choice=='c':
        number_of_products=int(input('Number of products: '))
        while number_of_products<MIN_PRODUCTS:
            print('Invalid input')
            number_of_products=int(input('Number of products: '))
        price=float(input('Price: '))
        while price<=MIN_PRICE:
            print('Invalid input')
            price=float(input('Price:'))
        if number_of_products >DISCOUNT_THRESHOLD: #apply 10% discount
            price *= DISCOUNT_RATE
        total_price = number_of_products * price
        print(f'{number_of_products} x ${price:.2f} products = ${total_price:.2f}')
    else:
        print('Invalid choice')
    print('Menu:')
    print('(I)nstructions')
    print('(C)alculate')
    print('(Q)uit')
    choice = input('Choice: ').lower()
print('Farewell')