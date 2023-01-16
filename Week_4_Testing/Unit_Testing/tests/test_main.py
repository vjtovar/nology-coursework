# import sys
# sys.path.insert(1, './code')
# from main import Point
import pytest
import sqlite3
# import requests
# import os


# def test_addition():
#     print("Addition Test - Begin")
#     assert add(2, 3) == 5
#     assert add(2, 4) == 6
#     assert add(5, 10) == 15
#     print("Addition Test - Complete")

# def add(a,b):
#     print("Assertion Iteration - Complete")
#     return a + b    


# def test_subtraction():
#     print("Subtraction Test - Begin")
#     assert subtract(2, 3) == -1
#     assert subtract(2, 4) == -2
#     assert subtract(5, 10) == -5
#     print("Subtraction Test - Complete")

# def subtract(a,b):
#     print("Subtraction Iteration - Complete")
#     return a - b


# # 1. Add multiply and divide to the Calc class code along code with accompanying test assertions
# # 2. Add a test case that checks that when you divide by 0, you get back the string "Can't divide by 0".
# # 3. Modify your divide function so it also passes the new test case.
# class TestCalculator:
#     def test_addition(self):
#         print("Test Calc Created for Addition Test")
#         calc = Calculator()
#         assert calc.add(5, 2) == 7
#         assert calc.add(2, 2) == 4
#         assert calc.add(15, 2) == 17
#         assert calc.add(9, 2) == 11
#         print("Test Completed for Addition Test")


#     def test_subtraction(self):
#         print("Test Calc Created for Subtraction Test")
#         calc = Calculator()
#         assert calc.subtract(5, 2) == 3
#         assert calc.subtract(10, 5) == 5 
#         assert calc.subtract(9, 3) == 6 
#         assert calc.subtract(6, 2) == 4   
#         print("Test Completed for Subtraction Test") 

#     def test_multiplication(self):
#         print("Test Calc Created for Multiplication Test")
#         calc = Calculator()
#         assert calc.multiply(2, 2) == 4
#         assert calc.multiply(3, 4) == 12 
#         assert calc.multiply(5, 5) == 25 
#         assert calc.multiply(7, 2) == 14   
#         print("Test Completed for Multiplication Test") 

#     def test_division(self):
#         print("Test Calc Created for Division Test")
#         calc = Calculator()
#         assert calc.divide(6, 2) == 3 
#         assert calc.divide(10, 5) == 2 
#         assert calc.divide(4, 2) == 2 
#         assert calc.divide(8, 2) == 4   
#         assert calc.divide(7, 0) == "Can't divide by 0"
#         print("Test Completed for Division Test")     

# class Calculator:
#     def add(self, a, b):
#         print("Addition Iteration Completed")
#         return a + b

#     def subtract(self, a, b):
#         print("Subtraction Iteration Completed")
#         return a - b    

#     def multiply(self, a, b):
#         print("Multiplication Iteration Completed")
#         return a * b   

#     def divide(self, a, b):
#         print("Division Iteration Completed")
#         try: 
#             return a / b
#         except ZeroDivisionError:
#             return "Can't divide by 0" 
        
     
# # ZeroDivisionError
# def test_division_by_zero():
#     with pytest.raises(ZeroDivisionError, match="division by zero"): #expect zerodivision error, so passes
#         division(10, 0)

# def division(a, b):
#     return a / b



# # Testing files
# def test_file_exists():
#     assert os.path.exists('./static/file.txt')

# def test_file_contents():
#     with open('./static/file.txt', 'r') as f:
#         contents = f.read()
#     assert contents == "The contents of this file"   

# def test_file_creation():
#     create_file('./static/new_file.txt')
#     assert os.path.exists('./static/new_file.txt')

# def create_file(path):
#     with open(path, 'w') as f:
#         f.write('contents of new file')

# def test_new_file_contents():
#     with open('./static/new_file.txt', 'r') as f:
#         contents = f.read()
#     assert contents == 'contents of new file'


# #class in main.py
# def test_make_point():
#     point = Point("Waco", 34, 34)
#     assert point.get_lat_long() == (34, 34)



# @pytest.fixture
# def setup_database():
#     conn = sqlite3.connect(":memory:")
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")
#     sample_data = [
#         ('2020-01-01', 'BUY', 'IBM', 1000, 45.0),
#         ('2020-01-01', 'SELL', 'TSLA', 352, 200.0),
#     ]
#     cursor.executemany("INSERT INTO stocks VALUES(?, ?, ?, ?, ?)", sample_data)
#     yield conn

# def test_connection(setup_database):
#     cursor = setup_database
#     assert len(list(cursor.execute('SELECT * FROM stocks'))) == 2    



# @pytest.mark.parametrize("inputs, expected_output", [
#     ([2, 3], 5),
#     ([-2, 3], 1),
#     ([2, -3], -1),
#     ([0, 0], 0),
# ])
# def test_addition(inputs, expected_output):
#     print("\n Addition Iteration - Test Start")
#     assert add(inputs[0], inputs[1]) == expected_output

# def add (a, b):
#     return a + b











