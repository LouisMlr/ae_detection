# Adverse Effect Detection

## Setup

1. Navigate into the project directory

   ```bash
   $ cd openai-quickstart-python
   ```

2. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

3. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

4. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

## Start the application

1. Run the FastAPI service

   ```bash
   $ uvicorn main:app --reload
   ```

FastAPI service is running a[http://127.0.0.1:80](http://127.0.0.1:80)!

2. Run the Streamlit App

   ```bash
   $ streamlit run app.py
   ```

Streamlit App is running at [http://127.0.0.1:8501](http://127.0.0.1:8501)!

## Start the application with Docker

1. Launch the services using docker-compose

   ```bash
   $ docker-compose build
   $ docker-compose up
   ```
