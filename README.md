# LEGO® IR Blaster

## Description

You can control LEGO® Power Functions with this Flask application if you install it on a Raspberry Pi.

Check the video below to see it in action!

## Video

https://www.youtube.com/watch?v=HI0b8D8LjN8

## To-do list

* Unit tests for jQuery
* Write documentation on how to get this running on Raspberry Pi
* Write documentation on the used hardware (IR led, transistor, etc.)

## References

* http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/
* https://github.com/iConor/lego-lirc

## Virtual environment

Move to the project directory and type:

```
virtualenv -p python3 --no-site-packages venv
```

Activate the virtual environment like this:

```
source venv/bin/activate
```

Install the dependencies through PIP:

```
pip install -r requirements.txt
```

## Unit tests

Enable the virtual environment and move to the project directory.

To execute the unit tests, type:

```
python -m unittest
```

## Coverage

Enable the virtual environment and move to the project directory.

To execute the coverage, type:

```
coverage run --source=. -m unittest
```

To show the coverage report, type:

```
coverage report -m
```

## LIRC

To install LIRC on the Raspberry Pi, type:

```
sudo apt-get install lirc
```

Add the following lines to the **/etc/modules** file:

```
lirc_dev
lirc_rpi gpio_in_pin=23 gpio_out_pin=22
```

Change the **/etc/lirc/hardware.conf** file to:

```
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
```

Restart **lircd** so that it picks up the changes.

```
sudo /etc/init.d/lirc stop
sudo /etc/init.d/lirc start
```

Modify the **/boot/config.txt** file and add:

```
dtoverlay=lirc-rpi,gpio_in_pin=23,gpio_out_pin=22
```