import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime
# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
# Use an f-string to print the current
# day of the week and the current time.


def main():
    try:
        current_date_and_time = datetime.now()
        products_dict = read_dictionary('week_5/grocery_store_project/products.csv', 0)
        print('Inkom Emporium')
        with open('week_5/grocery_store_project/request.csv', "rt") as csv_file_2:
            reader = csv.reader(csv_file_2)
            next(reader)
        
            subtotal = 0
            total_items = 0
            sales_tax = .06 
            for line in reader:
                line[0] in products_dict
                print(f'{products_dict[line[0]][1]}: {line[1]} @ ${products_dict[line[0]][2]}')
                quantity = int(line[1])
                item_cost = float(products_dict[line[0]][2])
                subtotal += quantity * item_cost
                total_items += int(line[1])
            sales_tax_total = (subtotal * sales_tax) 
            total = subtotal + sales_tax_total       
            
            print(f'Number of Items: {total_items}')  
            print(f'Subtotal: ${subtotal:.2f}')    
            print(f'Sales Tax: {sales_tax_total:.2f}')          
            print(f'Total: ${total:.2f}')
            print(f'Thank you for shopping at the Inkom Emporium.')
            print(f"{current_date_and_time:%c}")
            
        customer_survey('week_5/grocery_store_project/customer_satisfaction.txt')
    except FileNotFoundError as not_found_err:
        print(f"Error: missing file")
        print(f'{not_found_err}')
    except PermissionError as perm_err:
        print(f"Error: {perm_err}") 
    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file {key_err}")

    
            
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    product_dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]
                # Store the data from the current
                # row into the dictionary.
                product_dictionary[key] = row_list
    # Return the dictionary.
    return product_dictionary

def customer_survey(filename):
    customer_satisfaction = int(input('On a scale of 1 to 10 how satisfied are you with this software? '))
    customer_report = input("Feel free to leave feedback on experience at Inkom Emporium down below: ")
    with open('week_5/grocery_store_project/customer_satisfaction.txt', "at") as customer_experience:
        customer_experience.write(f'\nCustomer Satisfaction Rating: {customer_satisfaction} \n{customer_report}\n')

if __name__ == "__main__":
    main()