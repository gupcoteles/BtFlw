# BtFlw

a simple xpath checker

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
Usage:
     python3 BtFlw.py [Flags]

Flags:
     -s, --site     access the site
     -pi, --xpathid allow specifying the xpath ID
     -b, --browser  Use to set browser(firefox/chrome/edge)

Example:
     python3 BtFlw.py -s <site name>.com -pi <xpath id> -b <firefox/chrome/edge>
     python3 BtFlw.py --site <site name>.com --xpathid <xpath id> --browser <firefox/chrome/edge>
```
