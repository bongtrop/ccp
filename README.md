# ccp

The copy and paste program with clip-server use stdin and stdout.

Github [https://github.com/bongtrop/ccp](https://github.com/bongtrop/ccp)

## Requirements

- Python 2 but i think that code can use in python 3
- Python module that you can see in requirements.txt

## Installation

It's simple like the other python project.

### pip 

```bash
pip install git+https://github.com/bongtrop/ccp.git
```

### Manual

```bash
git clone https://github.com/bongtrop/ccp.git
cd ccp
pip install -r requirements.txt
python setup.py install
```

## Usage

just ```ccp -h```

```bash
copy paste program with clip-server use stdin and stdout

Usage:      ccp copy <name> [-p <password>]
            ccp paste <name> [-p <password>]

            Option:     -e Encrypt with secret key

            Example:    echo "this_is_data" | ccp copy this_is_name
                        ccp paste this_is_name
```

## Contribution

I dont mind the way that you will contribute. Just do it. below is example.

- email
- create issue
- pull request
- carrier pigeon
- tell my friend to tell me
- foo bar

## License

Please see [LICENSE](LICENSE) file.