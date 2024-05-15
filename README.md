# Gemini Chatbot Application

## Overview

Gemini Chatbot Application is a project aimed at creating a chatbot application using Streamlit for the frontend interface and Gemini model API for backend processing. The chatbot allows users to input text queries, which are then processed by connecting to a database, running relevant SQL queries, and returning the output as a response on the chat interface.

## Getting Started

Follow these steps to set up the project:

1. **Create Git Repository**: Create a GitHub repository and clone it locally.

2. **Set Up Virtual Environment**: Set up a virtual environment and install the required dependencies from `requirements.txt`.

    ```bash
    conda create -p geminisql python==3.10 -y
    conda activate geminisql
    pip install -r requirements.txt
    ```

    Add the virtual environment directory (`geminsql/`) to `.gitignore` to exclude it from version control.

3. **Obtain API Key**: Get your API key from [here](https://makersuite.google.com/app/apikey) and add it to a new `.env` file.

4. **Create Database**: Add code to `splite.py` file to create a SQLite database (`student.db`) and execute it using `python sqlite.py`.

5. **SQL Queries**: Create a `sql.py` file and add code to execute SQL queries against the database.

6. **Run the Application**: Run your Streamlit app using `streamlit run sql.py`.

## Usage

After completing the setup steps, access the Streamlit app through the provided URL. Input text queries into the chat interface, and the application will connect to the database, run the relevant SQL queries, and display the output as responses on the chat interface.

## Contributors

- [Your Name](https://github.com/yourusername)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
