# Lego IR Blaster

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