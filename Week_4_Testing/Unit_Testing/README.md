# Unit_Testing

## Project: Intro to unit testing

### Overview
An adventure game built in Python and unit testing performed with pytest

### Specifications
1. Install python
2. Set up virtual environment
3. Install pyenv
4. Install pytest
5. Use pytest to test adventure game

### Python Installation 
1. Python3 - Download the latest version of python from the python site. run: ```brew install python3```. This should also install pip3. To check Python version, run: ```python3 --version```.
2. pip3 - To check if pip3 is already installed, run: ```pip3 --version```. The output should
be similar to pip 22.2.1.

### Virtual Environment Installation
1. Install virtual env package: ```pip3 install virtualenv```. Only needs to be done once, when first installing python.
2. Make directory for env: ```mkdir unit-testing && cd unit-testing```
3. Create environment: ```python3 -m venv env```
4. Activate environment: ```source env/bin/activate```. (env) indicates environment is active. 
5. run: ```brew install pyenv```. Only needs to be installed once. Check the version of pyenv, run: ```pyenv --version```.
6. If pyenv version not 3.10.7, run: ```pyenv install 3.10.7```
7. Change the local version to 3.10.7, run: ```pyenv local 3.10.7```
8. run: ```pyenv local``` to check the version of pyenv

### Pytest Installation
1. Install pytest, run: ```pip3 install pytest```
2. Create requirements.txt file and add requirements
3. run: ```pip3 install -r requirements.txt```, to install requirements
4. run: ```pytest -v -s```, to run tests on application
5. Add pytest-html to requirements.txt file
6. run: ```pip3 install pytest-html```, to install pytest-html
7. run: ```pytest --html=report.html```, this will add report.html file
8. Open live server to see report of tests

#### Testing Challenges
1. Add multiply and divide to the Calc class code along code with accompanying test assertions
2. Add a test case that checks that when you divide by 0, you get back the string "Can't divide by 0".
3. Modify your divide function so it also passes the new test case.

```
class TestCalculator:
    def test_addition(self):
        print("Test Calc Created for Addition Test")
        calc = Calculator()
        assert calc.add(5, 2) == 7
        assert calc.add(2, 2) == 4
        assert calc.add(15, 2) == 17
        assert calc.add(9, 2) == 11
        print("Test Completed for Addition Test")


    def test_subtraction(self):
        print("Test Calc Created for Subtraction Test")
        calc = Calculator()
        assert calc.subtract(5, 2) == 3
        assert calc.subtract(10, 5) == 5 
        assert calc.subtract(9, 3) == 6 
        assert calc.subtract(6, 2) == 4   
        print("Test Completed for Subtraction Test") 

    def test_multiplication(self):
        print("Test Calc Created for Multiplication Test")
        calc = Calculator()
        assert calc.multiply(2, 2) == 4
        assert calc.multiply(3, 4) == 12 
        assert calc.multiply(5, 5) == 25 
        assert calc.multiply(7, 2) == 14   
        print("Test Completed for Multiplication Test") 

    def test_division(self):
        print("Test Calc Created for Division Test")
        calc = Calculator()
        assert calc.divide(6, 2) == 3 
        assert calc.divide(10, 5) == 2 
        assert calc.divide(4, 2) == 2 
        assert calc.divide(8, 2) == 4   
        assert calc.divide(7, 0) == "Can't divide by 0"
        print("Test Completed for Division Test")     

class Calculator:
    def add(self, a, b):
        print("Addition Iteration Completed")
        return a + b

    def subtract(self, a, b):
        print("Subtraction Iteration Completed")
        return a - b    

    def multiply(self, a, b):
        print("Multiplication Iteration Completed")
        return a * b   

    def divide(self, a, b):
        print("Division Iteration Completed")
        try: 
            return a / b
        except ZeroDivisionError:
            return "Can't divide by 0" 
```            


#### Adventure Game Testing

```
def test_file_exists():
    assert os.path.exists('./code/adventure_game.py')
    assert os.path.exists('./test.log')


def test_file_contents():
    with open('./test.log', 'r') as f:
        contents = f.read()
    assert "This is a Debug msg" in contents    



def test_get_name():  
    set_keyboard_input(["Val"]) 
    intro_scene()
    output = get_display_output()
    assert output == ["What is your name adventurer: ", f"""
                        ☠️☠️☠️ Val, you are lost on a deserted island! ☠️☠️☠️
    """, """
                Your airplane had an engine blow out and you crash landed on an island. 
                You wake up washed ashore and realize you are alone, the only survivor, 
                with only the clothes on your back and a desire to survive.
    """]
    assert set_keyboard_input != "", "You didn't key in any name"



def test_directions():
    set_keyboard_input(["North","South", "East", "West"])
    choice_1()
    output = get_display_output()
    assert "What direction would you like to go? (North, South, East, or West): " in output
```    

#### Adventure Game Test Report
![Screenshot 2023-01-10 at 2 45 39 PM](https://user-images.githubusercontent.com/104322947/211678800-8d4539a2-f6e6-45c4-b265-dcaba15c4515.png)


