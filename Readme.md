# Task Management API

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pytest](https://img.shields.io/badge/Testing-pytest-green)

## 📌 Overview

This project is a RESTful API for task management developed as an academic assignment.

It demonstrates backend development fundamentals, including REST API design, file-based data storage, and unit testing.

## ⚙️ Features

- Retrieve all tasks  
- Retrieve a specific task by ID  
- Create new tasks  
- Delete tasks  

## 📡 API Endpoints

- GET /tasks → Get all tasks  
- GET /tasks/:id → Get a task by ID  
- POST /tasks → Create a new task  
- DELETE /tasks/:id → Delete a task  

## 💾 Data Storage

Tasks are stored locally in a `tasks.txt` file using JSON format.

## 🧪 Testing

Unit tests are implemented using **pytest** to ensure correct API behavior.

## 🚀 Installation & Usage

Clone the repository:

git clone <your-repo-url>  
cd <repo-folder>  

Install dependencies:

pip install -r requirements.txt  

Run the application:

python app.py  

Run tests:

pytest  

## 🎯 Purpose

This project was created to demonstrate practical skills in REST API development, backend logic, file-based data handling, and automated testing with pytest.

## 👩‍💻 Author

- Panagiota-Spyridoula Nikolidaki (https://github.com/PanagiotaNikol)
