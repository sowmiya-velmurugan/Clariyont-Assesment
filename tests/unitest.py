import unittest
from db import *


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'your_test_db_name',
    'host': 'your_test_mongodb_connection_string'
}
db = MongoEngine(app)

class ProjectMetadataTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        # Clean up test data after each test
        db.connection.drop_database(app.config['MONGODB_SETTINGS']['db'])

    def test_create_project_metadata(self):
        # Prepare test data
        tenant_id = 'test_tenant_id'
        csv_file_location = 'test_csv_file_location'

        response = self.app.post('/project_metadata', json={'tenant_id': tenant_id, 'csv_file_location': csv_file_location})
        data = response.get_json()

        # Verify the response
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertIn('tenant', data)
        self.assertIn('csv_file_location', data)
        self.assertIn('model_evaluation_results', data)

        # Additional assertions if necessary

    def test_get_project_metadata(self):
        # Prepare test data
        project_metadata = ProjectMetadata(tenant='test_tenant', csv_file_location='test_csv_location',
                                           model_evaluation_results='test_results').save()

        # Make a GET request to retrieve project metadata
        response = self.app.get(f'/project_metadata/{project_metadata.id}')
        data = response.get_json()

        # Verify the response
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['tenant'], 'test_tenant')
        self.assertEqual(data['csv_file_location'], 'test_csv_location')
        self.assertEqual(data['model_evaluation_results'], 'test_results')


if __name__ == '__main__':
    unittest.main()
