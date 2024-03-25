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
echo
if widget_needed "Do you want a shortcut widget for the "; then
    mkdir -p ~/.termux/widget/dynamic_shortcuts
    mkdir -p /data/data/com.termux/files/home/.shortcuts
    chmod 700 -R /data/data/com.termux/files/home/.shortcuts
    cp sriparna.sh /data/data/com.termux/files/home/.shortcuts
    echo "sriparna" > /data/data/com.termux/files/home/.shortcuts/Sriparna
    echo "sriparna-gui" > /data/data/com.termux/files/home/.shortcuts/Sriparna-Gui
    chmod +x /data/data/com.termux/files/home/.shortcuts/Sriparna
    chmod +x /data/data/com.termux/files/home/.shortcuts/Sriparna-Gui
    mkdir -p /data/data/com.termux/files/home/.shortcuts/icons
    chmod -R a-x,u=rwX,go-rwx /data/data/com.termux/files/home/.shortcuts/icons
    cp logo.png /data/data/com.termux/files/home/.shortcuts/icons/Sriparna.png
    cp logo.png /data/data/com.termux/files/home/.shortcuts/icons/Sriparna-Gui.png
    cp Sriparna ~/.termux/widget/dynamic_shortcuts
    cp Sriparna-Gui ~/.termux/widget/dynamic_shortcuts
    echo
    echo -e "Shortcut widget is created!\nLong click on Termux:Widget app and select Termux shortcut\nThere you will get two scripts, drag them to your homescreen\nYou can directly run these scripts by clicking on them !"
else
    echo "Fine, widget will not be created !"
fi

echo
echo "Setup script is successful !"
echo 
