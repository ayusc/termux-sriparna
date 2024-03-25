#!/bin/bash

widget_needed() {
    local question="$1"
    local response

    while true; do
        read -p "$question (yes/no): " response
        case $response in
            [Yy]|[Yy][Ee][Ss]) return 0 ;;  # Return success for "yes" responses
            [Nn]|[Nn][Oo]) return 1 ;;      # Return failure for "no" responses
            *) echo "Please answer yes or no." ;;
        esac
    done
}

pkg update -y && pkg upgrade -y && pkg install termux-api -y &>/dev/null

# Workaround to check for Termux Api App Installation 
if timeout 5 termux-api-start&&termux-toast "Working ..." &>/dev/null; then
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

# Termux:Widget implementation 
if widget_needed "Do you want a shortcut widget for the "; then
    mkdir -p ~/.termux/widget/dynamic_shortcuts
    mkdir -p /data/data/com.termux/files/home/.shortcuts
    chmod 700 -R /data/data/com.termux/files/home/.shortcuts
    mkdir -p /data/data/com.termux/files/home/.shortcuts/tasks
    chmod 700 -R /data/data/com.termux/files/home/.shortcuts/tasks
    mkdir -p /data/data/com.termux/files/home/.shortcuts/icons
    cp sriparna.sh /data/data/com.termux/files/home/.shortcuts/tasks
    chmod -R a-x,u=rwX,go-rwx /data/data/com.termux/files/home/.shortcuts/icons
    cp logo.png /data/data/com.termux/files/home/.shortcuts/icons/sriparna.sh.png
    cp sriparna.sh ~/.termux/widget/dynamic_shortcuts

else
    echo "Fine, widget will not be created !"
fi

echo
echo "Setup script is successful !"
echo 
