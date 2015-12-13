from . import config

if config.USE_SQLITE:
    from .models_sqlite import *
else:
    from .models_filedb import *
