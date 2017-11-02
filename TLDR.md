# TL;DR

## Apache + Python

```
sudo apt-get update
sudo apt-get install vim
sudo apt-get install apache2 libapache2-mod-wsgi-py3
cd /var/www/html
sudo git clone https://github.com/braek/legoirblaster.git
sudo chown pi:pi legoirblaster
cd legoirblaster
sudo apt-get install virtualenv
virtualenv -p python3 --no-site-packages venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
sudo vim /etc/apache2/sites-available/legoirblaster.conf
```

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

```
sudo a2dissite 000-default
sudo a2ensite legoirblaster
sudo service apache2 restart
```

# LIRC

```
sudo apt-get install lirc
sudo vim /etc/modules
```

```
lirc_dev
lirc_rpi
```

```
sudo vim /etc/lirc/hardware.conf
```

```
LIRCD_ARGS="--uinput"
DRIVER="default"
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
```

```
sudo vim /boot/config.txt
```

```
dtoverlay=lirc-rpi:gpio_out_pin=22
```

```
/etc/lirc/lircd.conf
```

```
include "/var/www/html/legoirblaster/lirc/LEGO_Single_Output.conf"
```

```
sudo vim /etc/rc.local
```

```
sudo lircd -d /dev/lirc0
```

```
sudo reboot
```