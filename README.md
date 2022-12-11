# pac-for-mac-os
Poor implemetntation of MAC OS local web server to distribute .pac file with proxy rules.\
How to use:
1) U can create own .pac file with diffirent web browser like FireFox with extention ProxySwitchy Omega
2) Create directory at $HOME\
mkdir -p ~/.proxy
3) Move .pac file to this folder
4) Edit python-server.py script to use correct path to this folder and port
5) Move python-server.py to /usr/local/bin\
sudo mv python-server.py /usr/local/bin
6) Edit network settings to user .pac file at http://127.0.0.1:<port_from_python-server.py>
7) Create crontab job\
crontab -e\
\* * * * * /usr/bin/pgrep -f python-server.py; [ $? != 0 ] && /usr/local/bin/python-server.py
