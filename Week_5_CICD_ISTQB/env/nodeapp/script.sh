#!/bin/bash
echo -------------- Update source list --------------
sudo apt-get update -y

echo -------------- Install Python ------------------
sudo apt-get install software-properties-common -y

echo -------------- Download node v18 ---------------
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -

echo ------------------ Install node ----------------
sudo apt-get install -y nodejs -y

echo ------------------ Install npm -----------------
sudo apt-get install npm -y

echo ------------- Installing Apache ----------------
sudo apt install apache2 -y

echo ------------ Enabling Apache Proxy -------------
sudo a2enmod proxy
sudo a2enmod proxy_http

echo ------- Add nology Apache Proxy File -----------
cp /home/vagrant/env/nodeapp/nology-proxy.conf /etc/apache2/sites-available
echo ls -la /etc/apache2/sites-available

echo ------- Register nology Apache Proxy File ------
sudo a2ensite nology-proxy.conf

echo -------------- Restart Apache ------------------
sudo systemctl reload apache2

echo --------------- Move into App Folder -----------
cd ../vagrant/app
pwd

echo -------------- Install Dependancies ------------
npm install

echo -------------------- Run App -------------------
node index.js