import streamlit as st
import todo_functions as tf

todos = tf.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase my productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo...", key="new_todo")



