#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

if [ -d "/data/" ]; then
    echo "Folder already exists"
else
    sudo mkdir -p "/data/"
fi

if [ -d "/data/web_static/" ]; then
    echo "Folder already exists"
else
    sudo mkdir -p "/data/web_static/"
fi

if [ -d "/data/web_static/releases/" ]; then
    echo "Folder already exists"
else
    sudo mkdir -p "/data/web_static/releases/"
fi

if [ -d "/data/web_static/shared/" ]; then
    echo "Folder already exists"
else 
    sudo mkdir -p "/data/web_static/shared/"
fi

if [ -d "/data/web_static/releases/test/" ]; then
    echo "Folder already exists"
else
    sudo mkdir -p "/data/web_static/releases/test/"
fi

sudo touch /data/web_static/releases/test/index.html

content="<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>"
file="/data/web_static/releases/test/index.html"
echo "$content" | sudo tee "$file"

if [ -L "/data/web_static/current" ];
then
    rm "/data/web_static/current"
fi

target_link="/data/web_static/releases/test/"
sudo ln -s -f "$target_link" /data/web_static/current

data_folder="/data"
user="ubuntu"
group chown -R "$user":"$group" "$data_folder"

nginx_config="
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://www.github.com/MichaelOmoniyi/alx-system_engineering-devops/;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}"
echo "$nginx_config" | sudo tee /etc/nginx/sites-available/default >/dev/null
sudo service nginix restart
