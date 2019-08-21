import ulogging as logging
from .app import app
from . import views
import gc

def __main__(**params):
    gc.collect()
    logging.basicConfig(level=logging.INFO)

    # Preload templates to avoid memory fragmentation issues
    gc.collect()
    app._load_template('homepage.html')
    app._load_template('note.html')
    gc.collect()

    import micropython
    micropython.mem_info()
    app.run(debug=True, **params)

if __name__ == '__main__':
    __main__()
