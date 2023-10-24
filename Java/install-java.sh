#!/bin/bash

sudo mkdir -p /etc/apt/keyrings
sudo wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public |   sudo tee /etc/apt/keyrings/adoptium.asc
eval "$(grep VERSION_CODENAME /etc/os-release)"
sudo tee /etc/apt/sources.list.d/adoptium.list << EOM
deb [signed-by=/etc/apt/keyrings/adoptium.asc] https://packages.adoptium.net/artifactory/deb $VERSION_CODENAME main
EOM

sudo apt update -y
echo .
echo "Installing temurin"
sudo apt install -y temurin-17-jdk
echo .
java --version