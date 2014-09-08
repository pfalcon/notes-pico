all:

# This target prepares snapshot of all dependency modules, for
# self-contained install
lib: requirements.txt
	PIP_MICROPY_DEST=$$PWD pip-micropython install -r requirements.txt

run:
	MICROPYPATH=lib micropython -X heapsize=150000 main.py

clean:
	rm -rf lib
