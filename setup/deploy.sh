#!/bin/bash

[[ $# != 1 ]] && echo "Please provide a container name" && exit

CONTAINER="$1"

echo "Deploying LXD container..."

lxc launch ubuntu:bionic $CONTAINER
lxc config device add $CONTAINER home disk source=$HOME path=/mnt/home

echo "Install Git and Ansible..."

sleep 5  # Wait for container network connectivity.
lxc exec $CONTAINER -- apt update -y
lxc exec $CONTAINER -- apt install git software-properties-common -y
lxc exec $CONTAINER -- apt-add-repository --yes --update ppa:ansible/ansible
lxc exec $CONTAINER -- apt install ansible -y
lxc exec $CONTAINER -- apt autoremove -y

echo "Deploy with Ansible Pull..."

lxc exec $CONTAINER -- ansible-pull --connection=local -i 127.0.0.1, \
    -U https://github.com/knowark/procesark \
    -d /var/git/procesark setup/local.yml
