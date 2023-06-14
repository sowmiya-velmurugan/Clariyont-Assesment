from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from .models import  *

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'your_db_name',
    'host': 'your_mongodb_connection_string'
}
db = MongoEngine(app)

@app.route('/project_metadata', methods=['POST'])
def create_project_metadata():
    tenant_id = request.json.get('tenant_id')
    csv_file_location = request.json.get('csv_file_location')

    # Create a new ProjectMetadata record
    project_metadata = ProjectMetadata(
        tenant=tenant_id,
        csv_file_location=csv_file_location,
        model_evaluation_results=""
    )
    project_metadata.save()

    return jsonify(project_metadata)

@app.route('/project_metadata/<project_metadata_id>', methods=['GET'])
def get_project_metadata(project_metadata_id):
    project_metadata = ProjectMetadata.objects.get(id=project_metadata_id)
    return jsonify(project_metadata)
