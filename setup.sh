#!/bin/bash

pkg update &>/dev/null && pkg upgrade -y &>/dev/null

# Workaround to check for Termux Api App Installation 
if timeout 5 termux-toast "Working ..." &>/dev/null; then
        echo -e "\nTermux API app is already installed.\n"
else
        echo "Termux API app is not installed."
        # Open F-Droid link
        termux-open-url "https://f-droid.org/packages/com.termux.api/"       
        exit 1
fi

# List of packages to install
packages=("termux-api" "python" "openssl" "libexpat" "ffmpeg" "flac")

install_package() {
    pkg install -y $1 &>/dev/null
}

for pkg in "${packages[@]}"; do
    echo "Installing $pkg..."
    install_package "$pkg"
done

# Install python requirements 
echo "Installing python packages ..."
pip install -U -r requirements.txt
