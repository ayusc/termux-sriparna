#!/bin/bash

pkg update &>/dev/null && pkg upgrade -y &>/dev/null

# List of packages to install
packages=("termux-api" "python")

install_package() {
    pkg install -y $1 &>/dev/null
}

for pkg in "${packages[@]}"; do
    echo "Installing $pkg..."
    install_package "$pkg"
done
