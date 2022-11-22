#!/usr/bin/env python

import sys
#import tkMessageBox
from splinter import Browser

browser_executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
fineart_username = 'example@email.com'
fineart_password = 'password'
fineart_url_signin = "https://fineartamerica.com/loginartist.php"
fineart_url_upload = "https://fineartamerica.com/controlpanel/updateartwork.html?newartwork=true"
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


try:
    browser = Browser('chrome', **browser_executable_path)
except:
    #tkMessageBox.showinfo(title="Fine Art America Automation", message="ERROR: ")
    print("Error occured attempting to initiate browser")
    sys.exit(0)
#finally:
#    sys.exit(1)

# sign-in process
browser.visit(fineart_url_signin)
if browser.is_text_present('Artist Login'):
    browser.fill('username', fineart_username)
    browser.fill('password', fineart_password)
    button = browser.find_by_text('Login')
    button.click()
else:
    print("Already signed into FAA")

# upload photo
browser.visit(fineart_url_upload)
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