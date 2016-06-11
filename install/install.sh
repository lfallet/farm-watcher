#!/bin/sh

# install necessary packages
sudo apt-get update && apt-get install -y python-serial python-smbus i2c-tools supervisor
sudo pip install virtualenv

# TODO assert Python version

# TODO create database

# link supervisor conf
sudo ln -s ~/farm_watcher/install/launch_flask_at_startup.conf /etc/supervisor/conf.d/
sudo supervisorctl reread
sudo supervisorctl update

