#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi
sudo mkdir -p /data/
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

echo "<html>
<head>
</head>
<body>Hello World</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/current /data/web_static/releases/test/

sudo chown -R ubuntu:ubuntu /data/

if ! sudo grep -q "location /hbnb_static/" /etc/nginx/sites-enabled/default; then
    sudo sed -i '/server_name _;/a location /hbnb_static/ {\n\talias /data/web_static/current/
;\n}' /etc/nginx/sites-enabled/default
fi

sudo service nginx restart
