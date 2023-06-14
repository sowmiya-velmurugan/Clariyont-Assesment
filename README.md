# Clariyont-Assesment

**Step1 : Create Virtual environment using CMD**

Run  python -m venv venv.
Activate the virtual environment:
For Windows: venv\Scripts\activate.bat

**step2: Install the required dependencies:**

pip install -r requirements.txt

**step3: Set Up MongoDB:**

Make sure you have MongoDB installed and running on your system or have access to a MongoDB instance.
Update the MongoDB configuration in the Flask application code (app.config['MONGODB_SETTINGS']) with your MongoDB settings, including the database name and connection string.

**step4: Set Environment Variables:**

Create a .env file in the project directory.
Define the necessary environment variables in the .env file, such as CSV_FILE_LOCATION, TARGET_COLUMN, and API_URL.

**step5: Run the Flask Application:**

In the terminal or command prompt, navigate to the project directory.
Activate the virtual environment if you created one.
Run the Flask application:
In Windows: python -m flask run

You can now access the API endpoints using the provided routes, such as http://localhost:5000/project_metadata for creating project metadata and http://localhost:5000/project_metadata/<project_metadata_id> for fetching project metadata by ID.
Use Postman, or  web browser to send POST and GET requests to these endpoints.

