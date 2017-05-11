all:

# This target prepares snapshot of all dependency modules, for
# self-contained install
lib: requirements.txt
	micropython -m upip install -p lib -r requirements.txt

run:
	MICROPYPATH=lib micropython -X heapsize=150wK -m notes_pico

clean:
	rm -rf lib
