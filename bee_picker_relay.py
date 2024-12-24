#!/usr/bin/python3
import sys
import os
from subprocess import Popen
from functools import partial
import yaml

configuration = {}


if os.sys.platform == 'darwin' or os.sys.platform == 'linux':
    with open(os.environ['HOME']+'/.bee_picker.yaml') as file:
        configuration.update(yaml.load(file, Loader=yaml.FullLoader))
if os.sys.platform == 'windows' or os.sys.platform == 'win32':
    with open(os.environ['USERPROFILE']+'/.bee_picker.yaml') as file:
        configuration.update(yaml.load(file, Loader=yaml.FullLoader))

if os.sys.platform == 'darwin' and 'MacOSDefaultBrowser' in configuration and configuration['MacOSDefaultBrowser'] == True:
    from LaunchServices import LSSetDefaultHandlerForURLScheme, LSCopyDefaultHandlerForURLScheme
    if LSCopyDefaultHandlerForURLScheme("http") != 'org.cici.BeePickerRelay':
        LSSetDefaultHandlerForURLScheme("http","org.cici.BeePickerRelay")    
    if 'localnettesthost' in configuration:
        import requests
        data = requests.get('http://'+configuration['localnettesthost'],timeout=20)
        print(data.text)


print("Command line arguments:")
print(sys.argv)


Popen(['open','/Applications/BeePicker.app','--args',sys.argv[1]])
