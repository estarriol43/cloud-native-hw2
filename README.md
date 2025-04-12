# cloud-native-hw2
## Environment
```bash
pip3 install -r requirements.txt
```

## Usage
```
usage: main.py [-h] {parity,add,factorial} ...

python math CLI

positional arguments:
  {parity,add,factorial}
    parity              parity checking
    add                 add operation
    factorial           factorial operation

options:
  -h, --help            show this help message and exit
```

## Run
```bash
# python3 main.py factorial 3
3! = 6
# python3 main.py add 1 2
1 + 2 = 3
# python3 main.py parity 1
1 is odd
```

## Run test
```bash
python3 -m unittest test.py
```

