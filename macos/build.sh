#!/bin/bash
pip3 install pyinstaller PyYAML pyobjc-framework-LaunchServices
python3 -m PyInstaller -w bee_picker_relay.py  --osx-bundle-identifier org.cici.BeePickerRelay --argv-emulation -n "Bee Picker Relay"
mv "dist/Bee Picker Relay.app" /Applications/
open "/Applications/Bee Picker Relay.app"
python3 -m PyInstaller -w bee_picker.py  --osx-bundle-identifier org.cici.BeePicker -n "BeePicker"
mv "dist/BeePicker.app" /Applications/
rm -r dist build *.spec
