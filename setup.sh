#!/bin/bash

pkg update -y && pkg upgrade -y && pkg install termux-api -y &>/dev/null

# Workaround to check for Termux Api App Installation 
if timeout 5 termux-api-start&&termux-api-stop&&termux-api-start&&termux-toast "Working ..." &>/dev/null; then
        :
else
        echo "Termux API app is not installed."
        # Open F-Droid link
        termux-open-url "https://f-droid.org/packages/com.termux.api/"       
        exit 1
fi

# List of packages to install
packages=("termux-api" "python" "openssl" "libexpat" "ffmpeg" "flac" "dialog")

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
