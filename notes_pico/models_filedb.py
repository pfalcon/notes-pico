from ucollections import OrderedDict
import filedb as uorm


db = uorm.DB("notes-db")

class Note(uorm.Model):

    __db__ = db
    __table__ = "note"
    __schema__ = OrderedDict([
        ("timestamp", ("TIMESTAMP", uorm.now)),
        ("archived", ("INT", 0)),
        ("content", ("TEXT", "")),
    ])

    @classmethod
    def mapkeys(cls, obj):
        return [obj.get(k) for k in cls.__schema__.keys()]

    @classmethod
    def public(cls):
        res = [x for x in cls.scan() if x.archived == 0]
        res.sort(key=lambda x: x.timestamp, reverse=True)
        return res
