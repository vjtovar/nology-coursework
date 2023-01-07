# Flask

## Project: Intro to flask

### Overview
A treasurehunt game built in HTML, CSS, JS, Python, and Flask

### Specifications
1. Install python
2. Set up virtual environment
3. Install pyenv
4. Install flask
5. Use flask to create http requests for different pages

### Python Installation 
1. Python3 - Download the latest version of python from the python site. run: brew install python3. This should also install pip3. To check Python version, run: python3 --version.
2. pip3 - To check if pip3 is already installed, run: pip3 --version. The output should
be similar to pip 22.2.1.

### Virtual Environment Installation
1. Install virtual env package: pip3 install virtualenv. Only needs to be done once, when first installing python.
2. Make directory for env: mkdir flask-api && cd flask-api
3. Create environment: python3 -m venv env
4. Activate environment: source env/bin/activate. (env) indicates environment is active. 
5. run: brew install pyenv. Only needs to be installed once. Check the version of pyenv, run: pyenv --version.
6. If pyenv version not 3.10.7, run: pyenv install 3.10.7
7. Change the local version to 3.10.7, run: pyenv local 3.10.7
8. run: pyenv local to check the version of pyenv
9. Install flask, run: pip3 install flask
10. Create app.py and add imports
11. run: export FLASK_APP=app.py
12. run: flask --debug run, to start the server

