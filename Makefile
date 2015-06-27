all:

# This target prepares snapshot of all dependency modules, for
# self-contained install
lib: requirements.txt
	# pip-micropython is deprecated
	#PIP_MICROPY_DEST=$$PWD pip-micropython install -r requirements.txt
	# This requires upip from https://github.com/micropython/micropython-lib/tree/master/upip
	# (see bootstrap_upip.sh)
	micropython -X heapsize=200wK -m upip install -p lib -r requirements.txt

run:
	MICROPYPATH=lib micropython -X heapsize=150wK -m notes_pico.main

clean:
	rm -rf lib
