from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()

customer_subtotal = float(input('What is your subtotal? '))

sales_tax_rate = .06
discount_rate = .1

if day_of_week == 2 or 3:
    if customer_subtotal >= 50:
        discount_amount = discount_rate * customer_subtotal

        discount_subtotal = customer_subtotal - discount_amount

        sales_tax_fifty_plus = sales_tax_rate * discount_subtotal

        fifty_plus_total = discount_subtotal + sales_tax_fifty_plus

        print(f'Discount Amount: ${discount_amount:.2f}')
        print(f'Sales Tax Amount: ${sales_tax_fifty_plus:.2f}')
        print(f'Total: ${fifty_plus_total:.2f}')

    else:
        under_fifty_sales_tax = sales_tax_rate * customer_subtotal

        under_fifty_total = customer_subtotal + under_fifty_sales_tax

        print(f'Sales Tax Amount: ${under_fifty_sales_tax:.2f}')
        print(f'Total: ${under_fifty_total:.2f}')

else:
    regular_sales_tax = sales_tax_rate * customer_subtotal
    reglar_total = customer_subtotal + regular_sales_tax
    print(f'Sales Tax Amount: ${regular_sales_tax:.2f}')
    print(f'Total: ${reglar_total:.2f}')