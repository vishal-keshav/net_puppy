![net_puppy_logo](net_puppy_logo.jpg)

# net_puppy
A network controlled puppy for command line interface

Uses push bullet service to control the linux command line interface from network
controlled device.

## How to use it?
The project is incomplete, however, it can be used in the current version by
followng the steps below:

### Step 1:

Create a account on [push bullet](https://www.pushbullet.com/).


### Step 2:

Login to your push bullet account, and under settings, Create Access Token
Note down the token


### Step 3:
```
vim pushbullet_test.py
```
In the __main__ function, fill up the token variable.


### Step 4:

Download push bullet [android app](https://play.google.com/store/apps/details?id=com.pushbullet.android&hl), and login.


### Step 5:
```
python pushbullet_test.py
```

### Step 6:

From androd app, type C space command.

For example: "C ls" for ls
