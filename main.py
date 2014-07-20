from app import app
import views

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    mem_info()
    app.run(debug=True)