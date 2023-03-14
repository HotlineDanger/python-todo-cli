import streamlit as st
import functions

todos = functions.get_todos()

st.title("Productivity app")
st.subheader("Improve your productivity")
st.write("This app improves your productivity")

for todo in todos:
    st.checkbox(todo)
