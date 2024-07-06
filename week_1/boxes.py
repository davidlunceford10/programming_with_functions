import math

number_of_manufactured_items = int(input('Enter the number of items: '))

items_per_box = int(input('Enter the number of items that you will pack per box: '))

box_count = math.ceil(number_of_manufactured_items / items_per_box)


print(box_count)

print(f'For {number_of_manufactured_items} items, packing {items_per_box} items in each box, you will need {box_count} boxes.')