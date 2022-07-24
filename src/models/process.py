import mongoengine as db
from datetime import datetime


class CityInfo(db.EmbeddedDocument):
    city_id = db.IntField()
    temperature = db.DecimalField()
    humidity = db.DecimalField()


class Process(db.Document):
    user_id = db.IntField(min_value=0, primary_key=True)
    datetime = db.DateTimeField(default=datetime.utcnow())
    data = db.ListField(
        field=db.EmbeddedDocumentField(CityInfo)
    )

    meta = {
        'indexes': [
            {
                'fields': ['$user_id'],
                'default_language': 'english'
            }
        ]
    }