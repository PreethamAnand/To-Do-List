import streamlit as st
import json
from datetime import datetime
import os

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def main():
    st.set_page_config(page_title="To-Do List", page_icon="📝")
    
    st.title("📝 To-Do List")
    st.write("Manage your tasks efficiently")
    
    # Initialize tasks in session state if not exists
    if 'tasks' not in st.session_state:
        st.session_state.tasks = load_tasks()
    
    # Add new task
    with st.form("add_task"):
        task_title = st.text_input("Task Title")
        task_description = st.text_area("Task Description")
        due_date = st.date_input("Due Date")
        priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        
        submitted = st.form_submit_button("Add Task")
        if submitted and task_title:
            new_task = {
                "id": len(st.session_state.tasks),
                "title": task_title,
                "description": task_description,
                "due_date": due_date.strftime("%Y-%m-%d"),
                "priority": priority,
                "completed": False,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.tasks.append(new_task)
            save_tasks(st.session_state.tasks)
            st.success("Task added successfully!")
    
    # Display tasks
    st.subheader("Your Tasks")
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        filter_status = st.selectbox("Filter by Status", ["All", "Completed", "Pending"])
    with col2:
        filter_priority = st.selectbox("Filter by Priority", ["All", "Low", "Medium", "High"])
    
    # Filter tasks
    filtered_tasks = st.session_state.tasks
    if filter_status != "All":
        filtered_tasks = [task for task in filtered_tasks if task["completed"] == (filter_status == "Completed")]
    if filter_priority != "All":
        filtered_tasks = [task for task in filtered_tasks if task["priority"] == filter_priority]
    
    # Display filtered tasks
    for task in filtered_tasks:
        with st.expander(f"{'✅' if task['completed'] else '⭕'} {task['title']} ({task['priority']})"):
            st.write(f"**Description:** {task['description']}")
            st.write(f"**Due Date:** {task['due_date']}")
            st.write(f"**Created:** {task['created_at']}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Toggle Complete", key=f"complete_{task['id']}"):
                    task["completed"] = not task["completed"]
                    save_tasks(st.session_state.tasks)
                    st.experimental_rerun()
            
            with col2:
                if st.button("Delete Task", key=f"delete_{task['id']}"):
                    st.session_state.tasks.remove(task)
                    save_tasks(st.session_state.tasks)
                    st.experimental_rerun()

if __name__ == "__main__":
    main() 