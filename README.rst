notes-pico
==========

Notes Pico is a simple note-taking web application. It was originally
written by Charles Leifer as a demo of how to write a simple, but slick
web application using the Flask web micro-framework. The application is
described in the blog post
http://charlesleifer.com/blog/saturday-morning-hack-a-little-note-taking-app-with-flask/
. Notes Pico is a port of this application to Picoweb web pico-framework
for MicroPython. It was ported by Paul Sokolovsky.

To install and run the application, you should install MicroPython
"Unix" port as described at https://github.com/micropython/micropython .
Once you have ``micropython`` executable in your PATH (recommended, but
not strictly necessary), change directory to where you want to install
the app (``~/tmp/`` should be good for a quick test) and install
``notes-pico`` package::

    micropython -m upip install -p app notes-pico

``app`` (argument of ``-p`` option) is a subdirectory into which to
install the application. To run the app, execute::

    MICROPYPATH=app micropython -m notes_pico

This will initialize note storage and output a URL to open in a browser::

    * Running on http://127.0.0.1:8081/

Open the link and start adding notes (after typing text press "Add note"
button or press Ctrl+Enter). Note that Picoweb port is intended to be
simple and low-resource, so supports only plain-text notes, unlike the
original Flask application.


Storage backends
----------------

Notes Pico supports 3 storage backends:

* BTree
* Filesystem
* SQLite3

As a first step towards portability to MicroPython microcontroller
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

Currently, Notes Pico tested only with "Unix" MicroPython port,
though there's intention to make it work on microcontroller ports
with networking support and suitable resources.
