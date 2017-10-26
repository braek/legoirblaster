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

## Install Apache on Raspbian

You can check the Raspbian version with the following command:

```
cat /etc/os-release
```

Check the Python 3 version with the following command:

```
python3 --version
```

Install Apache with the following command:

```
sudo apt-get install apache2 libapache2-mod-wsgi-py3
```

Check the Apache version with the following command:

```
apache2 -v
```

Install **virtualenv** with the following command:

```
sudo apt-get install virtualenv
```

Move to the Apache web directory:

```
cd /var/www/html
```

Clone the project from GitHub in this directory:

```
sudo git clone https://github.com/braek/legoirblaster.git
```

Change the owner of the project directory to user **pi** and group **pi** with the following command:

```
chown pi:pi legoirblaster
```

Move to the project directory:

```
cd legoirblaster
```

Create a virtualen environment **venv** inside the project directory:

```
virtualenv -p python3 --no-site-packages venv
```

Activate the virtual environment:

```
source venv/bin/activate
```

Install the dependencies through PIP:

```
pip install -r requirements.txt
```

Deactivate the virtual environment:

```
deactivate
```

Add a new site in Apache 2:

```
sudo vim /etc/apache2/sites-available/legoirblaster.conf
```

And paste the following content in that file:

```
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
```

Disable the default site:

```
sudo a2dissite 000-default
```

Enable the project site:

```
sudo a2ensite legoirblaster
```

Restart Apache:

```
sudo service apache2 restart
```





## LIRC configuration

Install LIRC:

```
sudo apt-get install lirc
```

Add these lines to **/etc/modules** file:

```
lirc_dev
lirc_rpi gpio_out_pin=22
```

Change the **/etc/lirc/hardware.conf** file to:

```
LIRCD_ARGS="--uinput"
LOAD_MODULES=true
DRIVER="default"
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
LIRCD_CONF=""
LIRCMD_CONF=""
```

Uncomment this line in the **/boot/config.txt** file:

```
dtoverlay=lirc-rpi
```

Add this line to the **/etc/lirc/lircd.conf** file:

```
include "/home/pi/legoirblaster/lirc/LEGO_Single_Output.conf"
```

Restart the LIRC service:

```
sudo /etc/init.d/lirc restart
```

Start the **/dev/lirc0** device:

```
sudo lircd -d /dev/lirc0
```