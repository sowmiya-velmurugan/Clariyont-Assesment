from flask_mongoengine import MongoEngine

db = MongoEngine()

class Tenant(db.Document):
    name = db.StringField(required=True)


class ProjectMetadata(db.Document):
    tenant = db.ReferenceField(Tenant, required=True)
    csv_file_location = db.StringField(required=True)
    model_evaluation_results = db.StringField()

