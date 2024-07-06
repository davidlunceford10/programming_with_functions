import shutil
from colorama import Fore, Style, init
import ipaddress
import os
import time
import pytest
import subnet_calculator


def subnet_calculator(CIDR_network_ip_address, subnet_count):
    
    network = ipaddress.IPv4Network(f'{CIDR_network_ip_address}')

    network_portion_plus_subnet = network.prefixlen + (subnet_count - 1).bit_length()

    if network_portion_plus_subnet > 32:
        raise ValueError(f"Cannot divide {network} into {subnet_count} subnets. The required prefix length {network_portion_plus_subnet} is too large.")

    subnets = list(network.subnets(new_prefix=network_portion_plus_subnet))

    return subnets

subnets = subnet_calculator('192.168.10.0/24', 30)
print(subnets)