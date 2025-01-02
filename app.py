import time
import streamlit as st
import plotly.express as px
from gemini_calls import generate_sql_from_openai, execute_sql, validate_sql

avatar_url = "https://vanna.ai/img/vanna.svg"

st.set_page_config(layout="wide")

# Sidebar for Output Settings
st.sidebar.title("Output Settings")
st.sidebar.checkbox("Show SQL", value=True, key="show_sql")
st.sidebar.checkbox("Show Table", value=True, key="show_table")
st.sidebar.checkbox("Show Summary", value=True, key="show_summary")
st.sidebar.checkbox("Show Follow-up Questions", value=True, key="show_followup")
st.sidebar.checkbox("Show Plotly Chart", value=False, key="show_plotly")
st.sidebar.button("Reset", on_click=lambda: set_question(None), use_container_width=True)

# Main App
st.title("Gemini AI SQL Generator")

def set_question(question):
    st.session_state["my_question"] = question

assistant_message_suggested = st.chat_message("assistant", avatar=avatar_url)
if assistant_message_suggested.button("Click to show suggested questions"):
    st.session_state["my_question"] = None
    questions = ["What are the top products?", "How many sales were made last year?", "Which employees are the highest earners?"]  # Sample questions
    for i, question in enumerate(questions):
        time.sleep(0.05)
        st.button(question, on_click=set_question, args=(question,))

my_question = st.session_state.get("my_question", default=None)
if my_question is None:
    my_question = st.chat_input("Ask me a question about your data")

if my_question:
    st.session_state["my_question"] = my_question
    user_message = st.chat_message("user")
    user_message.write(f"{my_question}")

    try:
        # Generate SQL from OpenAI
        sql = generate_sql_from_openai(my_question)
