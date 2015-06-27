from .app import app
from . import views

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    import micropython
    micropython.mem_info()
    app.run(debug=True)