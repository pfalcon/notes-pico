TARGET = unix

.PHONY: lib mpy

all:

# This target prepares snapshot of all dependency modules, for
# self-contained install
lib: requirements.txt
	micropython -m upip install -p lib -r requirements.txt

run:
	MICROPYPATH=lib micropython -X heapsize=150wK -m notes_pico

res:
	cd notes_pico; mpy_bin2res.py static/js/* >R.py

mpy:
	mpy_cross_all.py notes_pico -o mpy/notes_pico --target=$(TARGET)
	mpy_cross_all.py lib -o mpy/lib --target=$(TARGET)
	cp -r notes_pico/static mpy/notes_pico

run-mpy:
	cd mpy; MICROPYPATH=lib micropython -X heapsize=50wK -m notes_pico

clean:
	rm -rf lib mpy
