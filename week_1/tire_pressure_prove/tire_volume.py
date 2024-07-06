from datetime import datetime
import math

current_date_and_time = datetime.now()


with open('week_1/tire_pressure_prove/volumes.txt', mode='at') as volume_datasheet:

    w = int(input('Enter the width of the tire in mm (ex 205): '))
    a = int(input('Enter the aspect ratio of the tire (ex 60): '))
    d = int(input('Enter the diameter of the wheel in inches (ex 15): '))

    #v = volume in liters#

    v = ((math.pi * (w ** 2) * a) * ((w * a) + 2540 * d ))/10000000000

    print(f'The approximate volume is {v:.2f} liters')

    buy_tires_yn = input('Do you want to buy tires with the entered dimensions? [yes/no]:').lower()
    if buy_tires_yn == "no":
        volume_datasheet.write(f'\n{current_date_and_time}, {w}, {a}, {d}, {v:.2f}')
    elif buy_tires_yn == 'yes':
        phone_number = int(input('What is your phone number? '))
        volume_datasheet.write(f'\n{current_date_and_time}, {w}, {a}, {d}, {v:.2f}, {phone_number}')

