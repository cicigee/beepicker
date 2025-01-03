# beepicker
Cross-platform link handler

- Interactive list of browsers / applications
- Let's you choose which browser or app to open when opening links
- Intelligent URI matching rules
- Keyboard shortcuts

Tested in Windows 10 / MacOS 12.6 Monterey / MacOS 14.4.1 Sonoma / MacOS 15.2 Sequoia / Ubuntu 20.04 Focal Fossa

## Screenshots

### MacOS 14.4.1:

![image](screenshot_macos14.png)

### MacOS 12.6:

![image](screenshot_macos12.png)

### Ubuntu Linux 20.04:

![image](screenshot_linux.png)

### Windows 10 21H2:

![image](screenshot_windows.png)


# Requirements
- Python 3.9+
- Tkinter

# Installation

## Package application (macOS and Windows)

https://pyinstaller.org/en/stable/

## Linux
```
mkdir -p /opt/ceeceepro
cp bee_picker.py /opt/ceeceepro/bee_picker.py
chmod +x /opt/ceeceepro/bee_picker.py
pip3 install tkinter
pip3 install PyYAML
```

## Configuring your rules & browsers

Customize your `.bee_picker.yaml` file.

## Setting as your default browser

### Windows
Import [registry entries](/windows/app_registration.reg)

```
SetUserFTA.exe https bee_picker.exe
SetUserFTA.exe http bee_picker.exe
```

SetUserFTA is available here: [kolbi.cz](https://kolbi.cz/blog/2017/10/25/setuserfta-userchoice-hash-defeated-set-file-type-associations-per-user/)

### MacOS

Run `macos/build.sh` with

##### Sequoia

set the `localnettesthost` (an IP address) key in `.bee_picker.yaml` to have MacOS prompt for lan access permissions, this can then be commented out in the configuration file after being prompted.

##### Sonoma (to set default browser manually)

Install the python3 module for LaunchServices with pip:
`pip3 install pyobjc-framework-LaunchServices`

Run this command in `python3` to set the default browser to BeePicker:
```
from LaunchServices import LSSetDefaultHandlerForURLScheme
LSSetDefaultHandlerForURLScheme("http","org.cici.BeePicker")
```

##### Monterey

Install [SwiftDefaultApps](https://github.com/Lord-Kamina/SwiftDefaultApps)

Select the app manually:
![image](screenshot_swiftdefaultapps.png)

(or https://sveinbjorn.org/platypus if you want to use it to build the app bundle)

### Linux
Use update-alternatives:

```
sudo update-alternatives --install /usr/bin/x-www-browser x-www-browser /opt/ceeceepro/bee_picker.py 200

update-alternatives --config x-www-browser
```
