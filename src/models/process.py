import mongoengine as db
from datetime import datetime


class Data(db.EmbeddedDocument):
    city_id = db.IntField()
    temperature = db.DecimalField()
    humidity = db.DecimalField()


class Process(db.Document):
    user_id = db.IntField(min_value=0, primary_key=True)
    datetime = db.DateTimeField(default=datetime.utcnow())
    data = db.ListField(
        field=db.MapField(db.EmbeddedDocumentField(Data))
    )

    meta = {
        'indexes': [
            {
                'fields': ['$user_id'],
                'default_language': 'english'
            }
        ]
    }