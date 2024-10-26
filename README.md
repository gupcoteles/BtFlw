# BtFlw

A simple xpath checker.

# Installation

```
python -m pip install -r requirements.txt
```

>[!NOTE]
>You Should have installed python

>[!TIP]
>You can install python from <a href="https://www.python.org/downloads/" target="_blank">here</a>.


# Usage

```
python BtFlw.py -h
```

This will display help for the tool. Here are all the switches it supports.

```
Usage:
     python BtFlw.py [Flags]

Flags:
     -s, --site     access the site
     -pi, --xpathid allow specifying the xpath ID
     -b, --browser  Use to set browser(firefox/chrome/edge)

Example:
     python BtFlw.py -s <site name>.com -pi <xpath id> -b <firefox/chrome/edge>
     python BtFlw.py --site <site name>.com --xpathid <xpath id> --browser <firefox/chrome/edge>
```
