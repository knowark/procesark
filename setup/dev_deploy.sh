#!/bin/bash

CONTAINER="procesark"

echo "Deploying development LXD container..."

lxc launch ubuntu:bionic $CONTAINER
lxc config device add $CONTAINER home disk source=$HOME path=/mnt/home

echo "Install Git and Ansible..."

sleep 5  # Wait for container network connectivity.
lxc exec $CONTAINER -- apt update -y
lxc exec $CONTAINER -- apt install git software-properties-common -y
lxc exec $CONTAINER -- apt-add-repository --yes --update ppa:ansible/ansible
lxc exec $CONTAINER -- apt install ansible -y
lxc exec $CONTAINER -- apt autoremove -y

# echo "Create database with its user..."

# lxc exec $CONTAINER -- su - postgres -c \
# "psql -c \"CREATE USER questionark WITH SUPERUSER PASSWORD 'questionark'\""

# lxc exec $CONTAINER -- su - postgres -c \
# "psql -c \"CREATE DATABASE questionark WITH OWNER questionark\""

# echo "Install virtualenv..."

# lxc exec $CONTAINER -- apt install python3-venv -y
# lxc exec $CONTAINER -- su - $USER -c "python3 -m pip install -U pip wheel"
# lxc exec $CONTAINER -- su - $USER -c "python3 -m venv /opt/questionark/env"

# echo "Link project to home..."

# lxc exec $CONTAINER -- ln -s $PROJECT_PATH /opt/$USER/questionark

# echo "Install virtualenv dependencies..."

# lxc exec $CONTAINER -- su - $USER -c "/opt/questionark/env/bin/python -m pip \
# install -U pip wheel"
# lxc exec $CONTAINER -- su - $USER -c "/opt/questionark/env/bin/python -m pip \
# install -r /opt/questionark/questionark/requirements.txt"

# echo "Open PostgreSQL port..."

# lxc exec $CONTAINER -- sh -c "cp $POSTGRES_CONF $POSTGRES_CONF.bkp"
# lxc exec $CONTAINER -- sh -c "cp $POSTGRES_PG_HBA $POSTGRES_PG_HBA.bkp"

# OLD="#listen_addresses = 'localhost"
# NEW="listen_addresses = '*"

# lxc exec $CONTAINER -- sed -i "s/${OLD}/${NEW}/g" $POSTGRES_CONF

# OLD="host    all             all             127.0.0.1\/32            md5"
# NEW="host    all             all             0.0.0.0\/0               md5"

# lxc exec $CONTAINER -- sed -i "s/${OLD}/${NEW}/g" $POSTGRES_PG_HBA

# OLD="host    all             all             ::1\/128                 md5"
# NEW="host    all             all             ::\/0                    md5"

# lxc exec $CONTAINER -- sed -i "s/${OLD}/${NEW}/g" $POSTGRES_PG_HBA

# echo "Restarting PostgreSQL..."

# lxc exec $CONTAINER -- service postgresql restart
