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
9. Install pytest, run: ```pip3 install pytest```
10. Create requirements.txt file and add requirements
11. run: ```pip3 install -r requirements.txt```, to install requirements
12. run: ```pytest -v -s```, to run tests on application
