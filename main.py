from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILE_NAME = "tasks.txt"

# Δημιουργία αρχείου αν δεν υπάρχει
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

def read_tasks():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def write_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Αρχική σελίδα - μόνο hints
@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Task API</title>
        </head>
        <body>
            <h1>Task Management API</h1>
            <p>Welcome. This API manages tasks in JSON format.</p>
            <p>Try exploring:</p>
            <ul>
                <li>/tasks → list all tasks</li>
                <li>/tasks/1 → view task with id 1</li>
            </ul>
            <p>Hint: Use GET, POST, DELETE requests.</p>
        </body>
    </html>
    """

# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    print("GET request: Επιστροφή όλων των tasks")
    return jsonify(read_tasks())

# Get task by id
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task_by_id(task_id):
    print(f"GET request: Αναζήτηση task με id {task_id}")
    tasks = read_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# Create task
@app.route("/tasks", methods=["POST"])
def create_task():
    tasks = read_tasks()
    data = request.get_json()

    new_id = 1 if not tasks else tasks[-1]["id"] + 1

    new_task = {
        "id": new_id,
        "username": data["username"],
        "title": data["title"],
        "description": data["description"],
        "deadline": data["deadline"]
    }

    tasks.append(new_task)
    write_tasks(tasks)


    return jsonify({"message": "Task created successfully"}), 201

# Delete task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = read_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    write_tasks(tasks)

    return jsonify({"message": "Task deleted successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


