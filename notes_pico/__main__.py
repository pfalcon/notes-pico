from .app import app
from . import views

def main():
    import logging
    logging.basicConfig(level=logging.INFO)
    import micropython
    micropython.mem_info()
    app.run(debug=True)

if __name__ == '__main__':
    main()
