# Fine Art America - Automated Image Uploader

FAA intentionally lacks any batch mechanism to upload images but manually doing each image is painful enough to where I decided to automate it. `FAA Automate` is a photography workflow tool (written in Python) that does the following:

- Export image from `Adobe Lightroom`
- Navigate to `Fine Art America (FAA)` gallery website
- Login to website
- Navigate to image import page
- Import image into `Fine Art America (FAA)`
- Provide opportunity to adjust default settings

## Requirements


## Build

Use the following steps to build the application:

```shell
# Download and unzip and move chromedriver to /usr/local/bin/ folder
SYSTEM_NAME=mac64 && LATEST_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$LATEST_VERSION/chromedriver_$SYSTEM_NAME.zip && sudo unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/;

# Create setup package
py2applet --make-setup --argv-emulation faa-automate.py
# Build the application
python setup.py py2app
# Remove any previous application
rm -rf /Applications/faa-automate.app
# Move the application to official destination
mv dist/faa-automate.app /Applications/
```

## TODO:

- complete entire upload process (image detail page is more complicated)

## References

- [splinter](https://splinter.readthedocs.io/en/latest/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- [py2app](https://py2app.readthedocs.io/en/latest/index.html)
- [Building and Distributing Packages with Setuptools](http://setuptools.readthedocs.io/en/latest/setuptools.html)
- [Creating standalone Mac OS X applications with Python and py2app](https://www.metachris.com/2015/11/create-standalone-mac-os-x-applications-with-python-and-py2app/)
- [py2app - Create standalone Mac OS X applications with Python](https://py2app.readthedocs.io/en/latest/index.html)
- [Simple Python Script to export photos from Adobe Lightroom](https://github.com/philroche/py-lightroom-export)
- [Qt Designer - alternative graphical interface designer](http://pyqt.sourceforge.net/Docs/PyQt4/designer.html)

## Issues

If you are using `pyenv` to create your Python environment you might hit the following error message:

`ValueError: '/Users/user/.pyenv/versions/3.11.0/lib/libpython3.11.dylib' does not exist`

In which case you need to rebuild your Python environment with this example:

`env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install -v 3.8.0`

## License

?

## Author

John Wadleigh