Demo minimalist custom skin for weewx
vinceskahan@gmail.com

This is a custom skin installable by the wee_extension utility.

Installation instructions:

1) run the installer:

wee_extension --install weewx-demo-skin.tgz

2) restart weewx:

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start

This will result in a skin called demo-skin that will write
into a 'demo-skin' subdirectory under your weewx HTML_ROOT

So if your weewx HTML_ROOT = /var/www/html/weewx
then to see the output of this skin you would 
open http://yourhostname/weewx/demo-skin in a browser.

