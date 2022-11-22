#!/usr/bin/env python

# Notes:
# - Exit python script using `sys.exit(n)` function; otherwise MacOS will get error code 255 instead
# - Max image size limit set by FAA is 25 MB

import sys
import os
#import tkMessageBox
from splinter import Browser
import yaml

config = yaml.safe_load(open(os.path.expanduser('~') + "/.faa-automate.yml"))
browser_executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
faa_username = config['username']
faa_password = config['password']
faa_url_signin = "https://fineartamerica.com/loginartist.php"
faa_url_upload = "https://fineartamerica.com/controlpanel/updateartwork.html?newartwork=true"
image_filename = ''

if len(sys.argv) >= 2:
    image_filename = sys.argv[1]
    #tkMessageBox.showinfo(title="Fine Art America Automation", message="we will import the file: " + image_filename)
    #sys.exit(0)
elif len(sys.argv) == 1:
    name = sys.argv[0]
    print("Not enough parameters")
    #tkMessageBox.showinfo(title="Fine Art America Automation", message="not enough parameters: " + name)
    sys.exit(0)
else:
    sys.exit(0)

if not faa_username or not faa_password:
    print("No FAA credentials found")
    sys.exit(0)

try:
    browser = Browser('chrome', **browser_executable_path)
except:
    #tkMessageBox.showinfo(title="Fine Art America Automation", message="ERROR: ")
    print("Error occured attempting to initiate browser")
    sys.exit(0)
#finally:
#    sys.exit(1)

# sign-in process
browser.visit(faa_url_signin)
if browser.is_text_present('Artist Login'):
    browser.fill('username', faa_username)
    browser.fill('password', faa_password)
    button = browser.find_by_text('Login')
    button.click()
else:
    print("Already signed into FAA")

# upload photo
browser.visit(faa_url_upload)
if browser.is_text_present('Upload New Image'):
    browser.fill('uploadimage', image_filename)
    button = browser.find_by_text('Upload Image')
    button.click()

if browser.is_text_present('Image Details'):
    # select galleries
    object = browser.find_by_id('galleryDiv')
    print(object)
    for g in object:
        print(g)
    # disable twitter
    button = browser.find_by_text('twitter')
    button.click()

    button = browser.find_by_text('Submit')
    button.click()