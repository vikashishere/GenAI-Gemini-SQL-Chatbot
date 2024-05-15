from dotenv import load_dotenv
load_dotenv() # Load all env var

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# configure genai Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to load Google Gemini model
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Funtion to retrieve query from the database
def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cur = connection.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    for row in rows:
        print(row)
    return rows

# Prompt designing
prompt = [
    """You are an expert in converting english questions to SQL query. 
    The SQL database has the name STUDENT and has the following columns -NAME, CLASS, SECTION. 
For example:
Example 1 - How many records are there in the STUDENTS table?
Response should be - select count(*) from STUDENT;
Example 2 - Give me the students details from "Data Science" class in the STUDENTS table.
Response should be - select * from STUDENT where CLASS="Data Science";
Also the sql code should not have ''' in the beginning or end and sql word in output"""
]

# Streamlit app
st.set_page_config(page_title="SQL Data Retriever")
st.header("Gemini powered bot to retrieve SQL data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, "student.db")
    st.subheader("Below is the response")
    for row in response:
        print(row)
        st.header(row)

