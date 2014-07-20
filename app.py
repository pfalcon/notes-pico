import picoweb
import models


class DBApp(picoweb.WebApp):

    def init(self):
        models.db.connect()
        models.Note.create_table(True)

app = DBApp()
