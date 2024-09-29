# Install Jupyter on Termux on Android
# 2024 - Termux 0.118.1, Python 3.11

## Setup Storage

```
$ termux-setup-storage
```
Allow

## Add Linux Repositories

```
$ pkg install x11-repo
$ pkg update
```

## Update Linux Packages

```
$ pkg upgrade
```

## Install Linux Packages

```
$ pkg install which
$ pkg install build-essential
$ pkg install libzmq
$ pkg install rust
$ pkg install python
```

## Install Python Virtual Environment

```
$ python -m venv v311
$ source v311/bin/activate
(v311) $ pip install setuptools
(v311) $ pip install cython
(v311) $ pip install pyzmq
(v311) $ pip install jupyter
```
It might be necessary to replace `pip install pyzmq` with `pip install pyzmq --config-settings="--zmq=/usr/lib"`.


## Add Symbols

```
(v311) $ pkg install -y patchelf
(v311) $ patchelf --add-needed libpython3.11.so v311/lib/python3.11/site-packages/zmq/backend/cython/_zmq.cpython-311.so
```

## Add Linux Packages

```
(v311) $ pkg install libjpeg-turbo
(v311) $ pkg install matplotlib
```
`libjpeg-turbo` is required for `matplotlib`. `matplotlib` should be installed via the Termux installer. 


## Add Python Packages

```
(v311) $ pip install numpy
```

## Start Jupyter

```
(v311) $ jupyter-notebook
```


# 2019

## Install Linux Packages
```
# Notice that there are no "-dev" packages. They have been merged into the
# remaining packages
apt install clang python fftw libzmq freetype libpng pkg-config

LDFLAGS="-L/system/lib/" CFLAGS="-I/data/data/com.termux/files/usr/include/" pip install Pillow

# Required for matplotlib
pkg install libjpeg-turbo
```

## Add scipy
```
# Add repository
curl -L https://its-pointless.github.io/setup-pointless-repo.sh | sh
pkg install scipy
```

## Install Python Packages
```
pip install wheel
pip install egg
pip install kiwisolver
pip install six
pip install cycler
pip install pyparsing
LDFLAGS=" -lm -lcompiler_rt" pip install numpy matplotlib pandas jupyter
```

## Run jupyter
```
jupyter notebook
```

## Run Remotely
```
# Consider setting remote password
jupyter notebook password

# Run remotely
jupyter notebook --no-mathjax --no-browser --ip 0.0.0.0 --port 8890
# The --no-mathjax improves loading over slow connections
```
