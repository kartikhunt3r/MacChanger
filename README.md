# MACChanger
Simple Mac Address Changer For Linux In python

![Logo](https://github.com/kartikhunt3r/MacChanger/blob/main/logo.gif)


## MAC Chain ⛓️

installation:

```bash
git clone https://github.com/kartikhunt3r/MacChanger.git

cd MacChanger

chmod +x *

python3 mac-chain.py --help
```

run:

```bash
python3 mac-chain.py -i wlan0 -t 20                   
```

options:

```bash
Usage: mac-proxychain.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Interface To Change Its MAC Address
  -t TIME, --time=TIME  time duration between changing each MAC address                 
```

## MacChanger

installation:

```bash
git clone https://github.com/kartikhunt3r/MacChanger.git

cd MacChanger

chmod +x *

python3 mac-changer.py --help
```

run:

```bash
python3 mac-changer.py -i wlan0 -m 11:22:33:44:55:66                  
```

options:

```bash
Usage: mac-changer.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Interface To Change Its MAC Address
  -m NEW_MAC, --mac=NEW_MAC
                        New MAC Address
```


## License



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


