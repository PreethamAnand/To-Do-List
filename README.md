# To-Do List App

A feature-rich To-Do List application built with Streamlit that helps you manage your tasks efficiently.

## Features

- Add, edit, and delete tasks
- Set task priorities (Low, Medium, High)
- Add due dates to tasks
- Mark tasks as complete/incomplete
- Filter tasks by status and priority
- Persistent storage using JSON
- Clean and intuitive user interface

## Setup

1. Make sure you have Python installed on your system
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the To-Do List app, navigate to the project directory and run:
```bash
streamlit run src/app.py
```

## Usage

1. Add a new task using the form at the top
2. View your tasks in the list below
3. Filter tasks by status or priority
4. Mark tasks as complete/incomplete
5. Delete tasks when they're no longer needed

## Data Storage

Tasks are stored in a `tasks.json` file in the project directory. The file is automatically created when you add your first task.
