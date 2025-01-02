import openai
import pandas as pd
import sqlite3
import streamlit as st

# Access the OpenAI API key from Streamlit's secrets
openai.api_key = st.secrets["openai"]["api_key"]

# SQLite Database Path
DB_PATH = '/home/ubuntu/open-streamlit/Chinook.sqlite'

# Function to generate SQL from OpenAI's GPT-3.5-turbo
def generate_sql_from_openai(question):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Translate the following question into an SQL query: {question}",
        max_tokens=150,
    )

    return response.choices[0].text.strip()

# Function to validate SQL by executing it on SQLite3
def validate_sql(sql):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(sql)  # Test if SQL is valid
        conn.close()
        return True
    except Exception as e:
        return False

# Function to execute the SQL query on SQLite3 and return the result as a DataFrame
def execute_sql(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Function to generate summary using OpenAI
def generate_summary(question, df):
    prompt = f"Provide a summary of prompt=prompt,
        max_tokens=200,
    )

    return response.choices[0].text.strip()

# Function to generate follow-up questions using OpenAI
def generate_followup_questions(question, sql, df):
    prompt = f"Suggest follow-up questions based on the question: {question}, SQL: {sql}, and data: {df.head(5)}"
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=200,
    )

    followups = response.choices[0].text.strip().split('\n')
    return followups following data based on the question: {question}\nData: {df.head(5)}"
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        
