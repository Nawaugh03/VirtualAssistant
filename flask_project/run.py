from app import create_app, db
from app.models import Task

# Initialize the app
app = create_app()

# Create the tables if they don't exist
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
