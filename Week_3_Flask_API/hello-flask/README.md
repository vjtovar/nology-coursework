
➜  ~ nology
➜  nology cd python-virtual-environments 
➜  python-virtual-environments cd hello-flask 
$  python3 -m venv env
➜  hello-flask source env/bin/activate                   

(env) ➜  hello-flask brew install pyenv
==> Fetching pyenv
==> Downloading https://ghcr.io/v2/homebrew/core/pyenv/manifests/2.3.9
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/pyenv/blobs/sha256:b88344e260fdf2f955
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:b
######################################################################## 100.0%
==> Pouring pyenv--2.3.9.arm64_ventura.bottle.tar.gz
🍺  /opt/homebrew/Cellar/pyenv/2.3.9: 979 files, 3.1MB
==> Running `brew cleanup pyenv`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
(env) ➜  hello-flask pyenv
pyenv 2.3.9
Usage: pyenv <command> [<args>]


(env) ➜  hello-flask pyenv install 3.10.7
python-build: use openssl@1.1 from homebrew
python-build: use readline from homebrew
Downloading Python-3.10.7.tar.xz...
-> https://www.python.org/ftp/python/3.10.7/Python-3.10.7.tar.xz
Installing Python-3.10.7...
python-build: use readline from homebrew
python-build: use zlib from xcode sdk
WARNING: The Python lzma extension was not compiled. Missing the lzma lib?
Installed Python-3.10.7 to /Users/vjtovar/.pyenv/versions/3.10.7

(env) ➜  hello-flask pyenv local 3.10.7
(env) ➜  hello-flask pyenv local
3.10.7
(env) ➜  hello-flask code .
(env) ➜  hello-flask 

$ pip3 install flask
(env) ➜  hello-flask export FLASK_APP=app.py
(env) ➜  hello-flask flask run or do flask --debug run             
 * Serving Flask app 'app.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
                                                                               
(env) ➜  hello-flask flask --debug run
 * Serving Flask app 'app.py'
 * Debug mode: on
