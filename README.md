# beepicker
Cross-platform link handler

- Interactive list of browsers / applications
- Let's you choose which browser or app to open when opening links
- Intelligent URI matching rules
- Keyboard shortcuts

Tested in Windows 10 / MacOS 12.6 Monterey / Ubuntu 20.04 Focal Fossa

## Screenshots

### MacOS 12.6:

![image](screenshot_macos.png)

### Ubuntu Linux 20.04:

![image](screenshot_linux.png)


# Requirements
- Python 3.9
- Tkinter

# Installation

# Setting as your default browser

## Windows
https://kolbi.cz/blog/2017/10/25/setuserfta-userchoice-hash-defeated-set-file-type-associations-per-user/

## MacOS
https://sveinbjorn.org/platypus

## Linux
Use update-alternatives:
`sudo update-alternatives --install /usr/bin/x-www-browser x-www-browser /opt/ceeceepro/bee_picker.py 200`
