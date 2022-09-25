#!/usr/bin/python3
import sys
import os
from subprocess import Popen
import tkinter
import tkinter.messagebox
from functools import partial
import yaml

configuration = {}

if os.sys.platform == 'darwin' or os.sys.platform == 'linux':
    with open(os.environ['HOME']+'/.bee_picker.yaml') as file:
        configuration.update(yaml.load(file, Loader=yaml.FullLoader))
if os.sys.platform == 'windows' or os.sys.platform == 'win32':
    with open(os.environ['USERPROFILE']+'/.bee_picker.yaml') as file:
        configuration.update(yaml.load(file, Loader=yaml.FullLoader))

print("Command line arguments:")
print(sys.argv)

print("Environmental variables:")
print(os.environ)

# Load yaml
rules = {}
browsers = {}

rules = configuration['rules']
default = configuration['default']
browsers = configuration['browsers']
browsers['default'] = browsers[default]


def shortcut_chooser(choice):
    choose(choice)


def choose(choice):
    global target_url, browsers, rule_matched, top, default, matched_browser
    print(f'Menu choice made: {choice}')
    if choice == 'matched browser':
        print(browser_launchers[matched_browser]+[target_url])
        Popen(browser_launchers[matched_browser]+[target_url])
    elif choice == 'default':
        print(browser_launchers[default]+[target_url])
        Popen(browser_launchers[default]+[target_url])
    elif choice == 'exit':
        pass
    else:
        print(browser_launchers[choice]+[target_url])
        Popen(browser_launchers[choice]+[target_url])
    top.destroy()


# Make sure there is an URL as an argument
if len(sys.argv) > 1:
    target_url = sys.argv[1]
else:
    print('No valid url specified')
    target_url = 'not_a_valid_url'
print(f'Input url: {target_url}')
print('Available browsers:')
browser_launchers = {}
for z in browsers:
    temp = browsers[z].replace(r'\ ', ';;;;').split(' ')
    line = []
    for space in temp:
        line.append(space.replace(';;;;', ' '))
    print(line)
    browser_launchers[z] = line

# Perform rule matching

rule_matched = 0
matcher = 'not_a_valid_url'

backward_rules = {}

if target_url != 'not_a_valid_url':
    print("Performing rule comparison:")
    for matcher in rules:
        for url in rules[matcher]:
            if url in backward_rules:
                print('duplicate rule')
            else:
                backward_rules[url] = matcher
            print(f'{url} == {target_url}?')

matched_percentage = 0
matched_browser = ''
for i in backward_rules:
    if i in target_url:
        print(f'{i} matches')
        matched_percentage1 = len(i)/len(target_url)*100
        print(f'{matched_percentage1}% match:'+i)
        if matched_percentage1 > matched_percentage:
            matched_percentage = matched_percentage1
            matched_browser = backward_rules[i]
            rule_matched = 1

print(f'Best rule match: {matched_browser} {matched_percentage}%')

if rule_matched == 1:
    print(f'should launch: {browsers[matched_browser]} {target_url}')
    message = f'Browser matches rule: {matched_browser}'
elif target_url == 'not_a_valid_url':
    print('No URL specified')
    message = 'No URL specified'
    browsers = {}
    target_url = 'N/A'
else:
    print('No browser rule matched, should run: {browsers[default]}')
    message = 'No browser rule matched'

top = tkinter.Tk(className='BeePicker')
top.eval('tk::PlaceWindow . center')

text = tkinter.Text(top, height=5)
if len(target_url) > 70:
    presented_url = target_url[0:67] + '...'
else:
    presented_url = target_url
text.insert(tkinter.INSERT, f'\n  URL: {presented_url}\n  '+message)
text.pack()

buttons = []

# Show matched browser button
if rule_matched == 1:
    buttons.append(tkinter.Button(top, text='matched browser',
                                  command=partial(choose, 'matched browser'),
                                  takefocus=True, padx=5, pady=5))
    buttons[len(buttons)-1].pack()
    top.bind('<Return>', lambda event: choose('matched browser'))

# Produce browser buttons
for i in browsers:
    print(f'Creating browser button for: {i}')
    buttons.append(tkinter.Button(top, text=i, command=partial(choose, i),
                                  padx=5, pady=5))
    buttons[len(buttons)-1].pack()

# Add cancel button
buttons.append(tkinter.Button(top, text='Cancel',
                              command=partial(choose, 'exit'),
                              padx=5, pady=5))
buttons[len(buttons)-1].pack()


if 'shortcuts' in configuration:
    for shortcut in configuration['shortcuts']:
        browser = ''
        browser = configuration['shortcuts'][shortcut]
        print(f'Binding keyboard shortcut: {shortcut} -> {browser}')
        top.bind(f'<{shortcut}>',
                 lambda event, choice=browser: shortcut_chooser(choice))
top.mainloop()
