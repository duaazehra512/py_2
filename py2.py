import streamlit as st
from datetime import datetime

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'task_input' not in st.session_state:
    st.session_state.task_input = ""

# Function to add a task
def add_task(task, priority):
    if task and not any(t['task'] == task for t in st.session_state.tasks):  # Ensure unique tasks
        st.session_state.tasks.append({
            "task": task,
            "priority": priority,
            "completed": False,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        sort_tasks()
        st.rerun()

# Function to remove a task efficiently
def remove_task(task_to_remove):
    st.session_state.tasks = [task for task in st.session_state.tasks if task["task"] != task_to_remove]
    st.rerun()

# Function to toggle completion
def toggle_task(task_name):
    for task in st.session_state.tasks:
        if task["task"] == task_name:
            task["completed"] = not task["completed"]
    st.rerun()

# Function to edit a task
def edit_task(old_task_name, new_task_name):
    for task in st.session_state.tasks:
        if task["task"] == old_task_name:
            task["task"] = new_task_name
    st.rerun()

# Function to sort tasks by priority
def sort_tasks():
    priority_order = {"🚨 High": 1, "⚖️ Medium": 2, "🟢 Low": 3}
    st.session_state.tasks.sort(key=lambda x: priority_order[x["priority"]])

# Function to clear all tasks efficiently
def clear_all_tasks():
    st.session_state.tasks = []
    st.rerun()

# App Title with emoji
st.markdown("""
    <h1 style='text-align: center; color: #FF6347;'>📝 Growth Mindset To-Do List ✅</h1>
""", unsafe_allow_html=True)

# Sidebar for Task Input with styling
st.sidebar.markdown("""
    <h1 style='color: #4CAF50;'>📋 Manage Your Tasks</h1>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
    <h2 style='color: black;'>✍️ Enter Your Task Here...</h2>
""", unsafe_allow_html=True)

task_input = st.sidebar.text_input("", key="task_input")

st.sidebar.markdown("""
    <h2 style='color: black;'>⚡ Priority</h2>
""", unsafe_allow_html=True)
priority_select = st.sidebar.selectbox("", ["🚨 High", "⚖️ Medium", "🟢 Low"], key="priority_select")

def reset_task_input():
    st.session_state.task_input = ""

if task_input:
    add_task(task_input, priority_select)
    st.button("✅ Confirm", on_click=reset_task_input)  # Ensures session state is updated safely

# Display Tasks with improved styling
if st.session_state.tasks:
    st.markdown("""
        <h2 style='color: #FFD700;'>📝 Your To-Do List</h2>
    """, unsafe_allow_html=True)
    
    sort_tasks()
    for index, task in enumerate(st.session_state.tasks):
        with st.container():
            cols = st.columns([4, 2, 2, 2])  # Adjusted column widths for better responsiveness
            
            # Task with priority tag
            with cols[0]:
                task_color = "green" if task["completed"] else "black"
                st.markdown(f"<h4 style='color: {task_color};'>{task['task']}</h4>", unsafe_allow_html=True)
                st.markdown(f"<small style='color: gray;'>{task['priority']}</small>", unsafe_allow_html=True)
                st.caption(f"🕒 Added: {task['timestamp']}")

            # Mark as completed (changes task color)
            with cols[1]:
                if st.checkbox("✔️ Done", task["completed"], key=f"check_{index}"):
                    toggle_task(task["task"])

            # Edit task button
            with cols[2]:
                new_task_name = st.text_input(f"✏️ Edit {task['task']}", value=task['task'], key=f"edit_{index}")
                if st.button("💾 Save", key=f"edit_btn_{index}"):
                    edit_task(task["task"], new_task_name)

            # Remove task button
            with cols[3]:
                if st.button("🗑️ Remove", key=f"remove_{index}"):
                    remove_task(task["task"])
else:
    st.info("🎉 No tasks added yet. Start by adding a task from the sidebar!")

# Clear all tasks button
if st.button("🗑️ Clear All Tasks"):
    clear_all_tasks()
