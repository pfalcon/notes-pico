notes-pico
==========

Notes Pico is a simple note-taking web application. It was originally
written by Charles Leifer as a demo of how to write a simple, but slick
web application using the Flask web micro-framework. The application is
described in the blog post
http://charlesleifer.com/blog/saturday-morning-hack-a-little-note-taking-app-with-flask/
. Notes Pico is a port of this application to the
[Picoweb](https://github.com/pfalcon/picoweb/) web pico-framework
for Pycopy (https://github.com/pfalcon/pycopy), a minimalist Python
implementation. It was ported by Paul Sokolovsky.


Deploying on Pycopy "Unix" version
----------------------------------

To install and run the application, you should install Pycopy
"Unix" port as described at https://github.com/pfalcon/pycopy .
Once you have ``pycopy`` executable in your PATH (recommended, but
not strictly necessary), change directory to where you want to install
the app (``~/tmp/`` should be good for a quick test) and install
``notes-pico`` package::

    pycopy -m upip install -p app notes-pico

``app`` (argument of ``-p`` option) is a subdirectory into which to
install the application. To run the app, execute::

    MICROPYPATH=app pycopy -m notes_pico

This will initialize note storage and output a URL to open in a browser::

    * Running on http://127.0.0.1:8081/

Open the link and start adding notes (after typing text press "Add note"
button or press Ctrl+Enter). Note that Picoweb port is intended to be
simple and low-resource, so supports only plain-text notes, unlike the
original Flask application.


Deploying on embedded Pycopy targets
------------------------------------

Notes Pico can also run on "embedded" (microcontroller) Pycopy
targets with networking capabilities and suitable heap size (TBC).
As Notes Pico is full-stack application and contains relatively a
lot of code, the only realistic way to deploy it on such systems is
using "frozen bytecode" approach, where pre-compiled Python modules
are made part of the binary firmware image to flash on the target.
Instructions below use Pycopy ESP8266 port as an example.

1. ``cd pycopy/ports/esp8266``
2. ``pycopy -m upip install -p modules notes-pico``
3. ``make``
4. ``make deploy`` (see README in the directory for more params)
5. Boot ESP8266 module, run following commands at the device prompt.
6. ``import notes_pico.__main__``
7. ``notes_pico.__main__.main(host="0.0.0.0")``
8. Connect with a web browser to http://`DEVICE_IP`:8081, where
   `DEVICE_IP` is an IP address of ESP8266 device. (Consult Pycopy
   ESP8266 port documentation for network connection setup.)


Storage backends
----------------

Notes Pico supports 3 storage backends:

* BTree
* Filesystem
* SQLite3

As a first step towards portability to Pycopy microcontroller
versions, the default backend for the package installed from PyPI
via the commands in the previous section is BTree database. The
notes are stored in ``notes.db`` database file of the current
directory, in BerkeleyDB 1.x format.

If you would like to try filesystem/SQLite3 backend, you'll need to
checkout https://github.com/pfalcon/notes-pico and edit file
``notes_pico/config.py``. The repository has a convenience
Makefile to install dependencies and run the application, similar
to the effect achieved by the commands above.


Known issues and limitations
----------------------------

As mentioned above, Picoweb port of the application supports only
plain-text notes, no formatting, images or videos.

Embedded targets support is experimental, added in version 0.8.
