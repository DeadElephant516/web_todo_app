import streamlit as st
import functions



todos = functions.get_todos()

def add_todo():
    todo = st.session_state["todo"].strip()
    if todo:
        todos.append(todo + "\n")
        functions.write_todos(todos)
    st.session_state["todo"] = ""  # Clear input box





st.title("My todo App")
st.subheader("This is my todo app :)")
st.write("This app helps you to increase your productivity")



for index,todo in enumerate(todos):
    if todo != "":
        checkbox = st.checkbox(todo, key=todo)

        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.rerun()

input_box = st.text_input("", placeholder="Enter a to do",
                          on_change=add_todo,key="todo")


st.session_state
