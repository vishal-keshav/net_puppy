![net_puppy_logo](net_puppy_logo.jpg)

# net-puppy
A light-weight and fast network controlled puppy for command line interface.
This enables you to control your linux terminal from your mobile application over a low latency network.

The program relies on the push bullet service to control the linux command line interface from a network
controlled device. The controller can be an another PC too, running a web browser for push notifications.

## Installation

For python 2
```
pip install net-puppy
```
or
```
python -m pip install net-puppy
```

For python 3
```
pip3 install net-puppy
```
or
```
python3 -m pip install net-puppy
```

## How to use it?
### Step 1:

Create a account on [push bullet](https://www.pushbullet.com/).


### Step 2:

Login to your push bullet account, and under settings, create an Access Token
Note down this token somewhere for future use.

## Additional Step 2:

Download push bullet [android app](https://play.google.com/store/apps/details?id=com.pushbullet.android&hl), and login with your push bullet credentials.


### Step 3:

Import the core module from net_puppy package in your python application.
```
python
>> from net_puppy import core
```


### Step 4:

Start the core module with start function, by providing your 34 character push bullet token.
```
>> core.start("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
```

### Step 5:

From androd app (n the ME tab), type "C <command>"
For example: "C ls" for ls on the terminal.

## Upcoming
In the next, full blown terminal info will be avalable in your push bullet app.
