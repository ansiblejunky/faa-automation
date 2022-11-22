# Fine Art America - Automated Image Uploader

Python tool to automate the uploading of images stored within `Adobe Lightroom` into my `Fine Art America (FAA)` gallery website. FAA does not provide any batch mechanism to upload images (intentional) but manually doing each image is painful enough to where I decided to automate it.

## Requirements

Install the following driver in a folder that is in the $PATH environment variable. For example, `/usr/local/bin`; and then edit the `executable_path` variable below.

- [splinter](https://splinter.readthedocs.io/en/latest/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- [py2app](https://py2app.readthedocs.io/en/latest/index.html)

## Notes

- make sure to exit python script using `sys.exit(n)` function; otherwise MacOS will get error code 255 instead
- make sure the generated setup.py has the following option to handle arguments:
      OPTIONS = {'argv_emulation': True}
- go headless browser using the following PhantomJS browser driver:
      http://splinter.readthedocs.io/en/latest/drivers/phantomjs.html

## Build

Use the following steps to build the application:

```shell
# Download chromedriver
# Unzip contents and right-click open the file to tell macOS that it is safe

# Verify the executable path for the chromedrive is specified in the python script)
mv chromedriver /usr/local/bin/chromedriver
# Create setup package
py2applet --make-setup fine-art-america-automate.py
# Install/setup package
python setup.py py2app
# Application now has been created and exists within the ./dist folder.
# Copy the application to your favorite location.
```

## TODO:

- add requirements.txt
- update README with instructions to use
- remove the use of Tk for windows and use command line instead
- bring browser to front
- complete entire upload process - image detail page is more complicated

## References

Automation:

- [Chrome WebDriver](http://splinter.readthedocs.io/en/latest/drivers/chrome.html)
- [Splinter - Python module to test and automate web applications](http://splinter.readthedocs.io/en/latest/index.html#)

GUI:

- [Qt Designer - alternative graphical interface designer](http://pyqt.sourceforge.net/Docs/PyQt4/designer.html)

Python:

- [Building and Distributing Packages with Setuptools](http://setuptools.readthedocs.io/en/latest/setuptools.html)
- [Creating standalone Mac OS X applications with Python and py2app](https://www.metachris.com/2015/11/create-standalone-mac-os-x-applications-with-python-and-py2app/)
- [py2app - Create standalone Mac OS X applications with Python](https://py2app.readthedocs.io/en/latest/index.html)

Lightroom:

- [](http://regex.info/blog/lightroom-goodies/run-any-command)
- [Simple Python Script to export photos from Adobe Lightroom](https://github.com/philroche/py-lightroom-export)

## Issues

If you are using `pyenv` to create your Python environment you might hit the following error message:

`ValueError: '/Users/user/.pyenv/versions/3.11.0/lib/libpython3.11.dylib' does not exist`

In which case you need to rebuild your Python environment with this example:

`env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install -v 3.8.0`

## License

?

## Author

John Wadleigh