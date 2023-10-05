#!/usr/bin/env bash
# This script sets up the web servers for the deployment of web_static
apt update -y >/dev/null 2>&1
apt install nginx -y >/dev/null 2>&1

mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" >/data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current
chown -hR ubuntu:ubuntu /data

sed -i '51i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

service nginx restart
