from flask import Blueprint, request, jsonify
from .models import Task, db
#from .utils import predict_label

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Welcome home!"})

@main.route('/hello')
def hello():
    return jsonify({"message": "Hello, World!"})

@main.route('/info')
def info():
    return jsonify({"info": "This is a simple Flask API"})

# Example route to create a task (POST request)
@main.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    
    if not title:
        return jsonify({"error": "Task title is required"}), 400
    
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify({"message": "Task created", "task": new_task.title}), 201

# Example route to get all tasks (GET request)
@main.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": task.id, "title": task.title, "completed": task.completed} for task in tasks])
