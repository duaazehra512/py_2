# import streamlit as st

# # To store the tasks, we'll use a session state.
# if 'tasks' not in st.session_state:
#     st.session_state.tasks = []

# # Function to add a task
# def add_task():
#     task = st.session_state.new_task
#     if task:
#         st.session_state.tasks.append(task)
#         st.session_state.new_task = ""  # Clear the input box

# # Function to remove a task
# def remove_task(task_to_remove):
#     st.session_state.tasks.remove(task_to_remove)

# # Title of the app
# st.title("Growth Mindset To-Do List")

# # Introduction
# st.markdown("""
# This is your personal To-Do list. Acknowledge each task and remove what's completed. 
# Keep growing with your tasks and progress!
# """)

# # Add Task Section
# st.subheader("Add a New Task:")
# st.text_input("Enter your task:", key="new_task")

# # Button to add task
# if st.button("Add Task"):
#     add_task()

# # Show current tasks in a beautiful, professional, and organized way
# if st.session_state.tasks:
#     st.subheader("Your Tasks:")
#     for task in st.session_state.tasks:
#         task_col, remove_col = st.columns([4, 1])  # Two columns: one for the task, one for removing the task
#         with task_col:
#             st.markdown(f"- {task}")
#         with remove_col:
#             if st.button("Remove", key=task):
#                 remove_task(task)
# else:
#     st.markdown("### No tasks added. Start by adding a task!")



import streamlit as st

# To store the tasks, we'll use a session state.
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'new_task' not in st.session_state:
    st.session_state.new_task = ""  # Initialize the new_task state

# Function to add a task
def add_task():
    task = st.session_state.new_task
    if task:
        st.session_state.tasks.append(task)
        st.session_state.new_task = ""  # Clear the input box after adding the task

# Function to remove a task
def remove_task(task_to_remove):
    st.session_state.tasks.remove(task_to_remove)

# Function to edit a task
def edit_task(old_task, new_task):
    index = st.session_state.tasks.index(old_task)
    st.session_state.tasks[index] = new_task

# Title of the app
st.title("Growth Mindset To-Do List")

# Introduction
st.markdown("""
This is your personal To-Do list. Acknowledge each task and remove what's completed. 
Keep growing with your tasks and progress!
""")

# Add Task Section
st.subheader("Add a New Task:")
# Using `st.session_state.new_task` as the initial value for the input box.
st.text_input("Enter your task:", key="new_task")

# Button to add task
if st.button("Add Task"):
    add_task()

# Show current tasks in a beautiful, professional, and organized way
if st.session_state.tasks:
    st.subheader("Your Tasks:")
    
    for task in st.session_state.tasks:
        # Creating columns for the task and the "Manage Task" box
        task_col, manage_col = st.columns([4, 2])  # Adjusted column sizes to fit the manage box

        with task_col:
            st.markdown(f"- **{task}**")
        
        with manage_col:
            # Create buttons for managing tasks (Edit and Remove)
            edit_button = st.button(f"Edit", key=f"edit_{task}")
            remove_button = st.button(f"Remove", key=f"remove_{task}")
            
            # If Remove button is clicked, remove the task
            if remove_button:
                remove_task(task)

            # If Edit button is clicked, show an input box to edit the task
            if edit_button:
                new_task = st.text_input(f"Edit task '{task}':", key=f"edit_input_{task}")
                if st.button("Save Changes", key=f"save_{task}"):
                    if new_task:
                        edit_task(task, new_task)
                    else:
                        st.warning("Task cannot be empty!")

else:
    st.markdown("### No tasks added. Start by adding a task!")
