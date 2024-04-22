#!/bin/bash
pip3 install pyinstaller PyYAML
python3 -m PyInstaller -w bee_picker.py  --osx-bundle-identifier org.cici.BeePicker --argv-emulation -n "Bee Picker"
mv "dist/Bee Picker.app" /Applications/
