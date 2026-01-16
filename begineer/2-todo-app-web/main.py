import streamlit as st
import todo_functions as tf


todos = tf.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo.title())
    tf.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase my productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        tf.append_completed(todo)
        todos.pop(index)
        tf.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add a new todo...", on_change=add_todo, key="new_todo")



