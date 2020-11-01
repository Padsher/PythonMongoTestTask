from umongo import Document, fields
from models.db import db, instance

@instance.register
class Product(Document):
    id = fields.ObjectIdField(attribute = '_id')
    name = fields.StringField()
    description = fields.StringField()
    properties = fields.DictField()
    class Meta:
        collection = db.product
    
    def toFullDict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'properties': self.properties
        }
    
    def toSmallDict(self):
        return {
            'id': str(self.id),
            'name': self.name
        }