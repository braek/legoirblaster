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

Include the Lego IR signals in the LIRC config in the **/etc/lirc/lircd.conf** file:

```
include "/var/www/html/legoirblaster/lirc/LEGO_Single_Output"
```

Start the LIRC device with this command:

```
sudo lircd -d /dev/lirc0
```

# Apache on Raspbian

TL;DR



sudo apt-get update



cat /etc/os-release
PRETTY_NAME="Raspbian GNU/Linux 9 (stretch)"
NAME="Raspbian GNU/Linux"
VERSION_ID="9"
VERSION="9 (stretch)"
ID=raspbian
ID_LIKE=debian
HOME_URL="http://www.raspbian.org/"
SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"



python3 --version
Python 3.5.3















sudo apt-get install apache2 libapache2-mod-wsgi-py3
apache2 -v













sudo apt-get install virtualenv
cd /var/www/html
sudo git clone https://github.com/braek/legoirblaster.git
chown pi:pi legoirblaster
cd legoirblaster
virtualenv -p python3 --no-site-packages venv
source venv/bin/activate
pip install -r requirements.txt
deactivate





sudo vim /etc/apache2/sites-available/legoirblaster.conf

<VirtualHost *:80>
    WSGIDaemonProcess legoirblaster python-home=/var/www/html/legoirblaster/venv user=pi group=pi threads=5
    WSGIScriptAlias / /var/www/html/legoirblaster/wsgi.py
    Alias /static /var/www/html/legoirblaster/legoirblaster/static
    <Directory /var/www/html/legoirblaster>
        WSGIProcessGroup legoirblaster
        WSGIApplicationGroup %{GLOBAL}
        Require all granted
    </Directory>
</VirtualHost>







sudo a2dissite 000-default
sudo a2ensite legoirblaster
sudo service apache2 restart
