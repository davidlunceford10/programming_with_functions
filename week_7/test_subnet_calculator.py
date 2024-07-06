import shutil
import pytest
from subnet_calculator import subnet_calculator, center_text

def main():
    test_subnet_calculator()
    test_center_text()
    

def test_subnet_calculator():
      
    correct_results_testcase_1 = "[IPv4Network('192.168.10.0/29'), IPv4Network('192.168.10.8/29'), IPv4Network('192.168.10.16/29'), IPv4Network('192.168.10.24/29'), IPv4Network('192.168.10.32/29'), IPv4Network('192.168.10.40/29'), IPv4Network('192.168.10.48/29'), IPv4Network('192.168.10.56/29'), IPv4Network('192.168.10.64/29'), IPv4Network('192.168.10.72/29'), IPv4Network('192.168.10.80/29'), IPv4Network('192.168.10.88/29'), IPv4Network('192.168.10.96/29'), IPv4Network('192.168.10.104/29'), IPv4Network('192.168.10.112/29'), IPv4Network('192.168.10.120/29'), IPv4Network('192.168.10.128/29'), IPv4Network('192.168.10.136/29'), IPv4Network('192.168.10.144/29'), IPv4Network('192.168.10.152/29'), IPv4Network('192.168.10.160/29'), IPv4Network('192.168.10.168/29'), IPv4Network('192.168.10.176/29'), IPv4Network('192.168.10.184/29'), IPv4Network('192.168.10.192/29'), IPv4Network('192.168.10.200/29'), IPv4Network('192.168.10.208/29'), IPv4Network('192.168.10.216/29'), IPv4Network('192.168.10.224/29'), IPv4Network('192.168.10.232/29'), IPv4Network('192.168.10.240/29'), IPv4Network('192.168.10.248/29')]"
    
    #call 1
    output = subnet_calculator('192.168.10.0/24', 30)

    #First assert
    assert f"{output}" == correct_results_testcase_1

    correct_results_testcase_2 = "[IPv4Network('189.10.1.0/28'), IPv4Network('189.10.1.16/28'), IPv4Network('189.10.1.32/28'), IPv4Network('189.10.1.48/28'), IPv4Network('189.10.1.64/28'), IPv4Network('189.10.1.80/28'), IPv4Network('189.10.1.96/28'), IPv4Network('189.10.1.112/28'), IPv4Network('189.10.1.128/28'), IPv4Network('189.10.1.144/28'), IPv4Network('189.10.1.160/28'), IPv4Network('189.10.1.176/28'), IPv4Network('189.10.1.192/28'), IPv4Network('189.10.1.208/28'), IPv4Network('189.10.1.224/28'), IPv4Network('189.10.1.240/28')]"
         
    #call 2
    output_2 = subnet_calculator('189.10.1.0/24', 12)

    #Second assert
    assert f"{output_2}" == correct_results_testcase_2

def test_center_text():
    text = "Try #1"
    terminal_width = shutil.get_terminal_size().columns
    centered_text = text.center(terminal_width)

    #call 1, assert 1
    assert center_text('Try #1') == centered_text

    text_2 = "Try #2"
    terminal_width = shutil.get_terminal_size().columns
    centered_text_2 = text_2.center(terminal_width)

    #call 2, assert 2
    assert center_text('Try #2') == centered_text_2




pytest.main(["-v", "--tb=line", "-rN", __file__])
    




