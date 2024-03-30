[Contribution guidelines for this project](docs/CONTRIBUTING.md)

# BtFlw

a simple xpath identity test finder

# Installation

```
python3 -m pip install -r requirements.txt
```

# Usage

```
python3 BtFlw.py -h
```

This will display help for the tool. Here are all the switches it supports.
```
Use:
     python3 BtFlw.py [Flags]

Flags:
     -s, --site access the site
     -pi, --xpathid allow specifying the xpath ID

Example:
     python3 BtFlw.py -s <site name>.com -pi "<xpath id>"
     python3 BtFlw.py --site <site name>.com --xpathid "<xpath id>"
```
