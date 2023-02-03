# Start from the official Python base image.
FROM python:3.10

# Set the current working directory to /code.
WORKDIR /streamlit

# Copy the file with the requirements to the /code directory.
COPY ./requirements.txt ./requirements.txt

# Install the package dependencies in the requirements file.
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# Copy the ./app directory inside the /code directory.
COPY . /streamlit

EXPOSE 8501

# Set the command to run the uvicorn server.
CMD ["streamlit", "run", "app.py"]



# The --no-cache-dir option tells pip to not save the downloaded packages locally,as that is only if 
# pip was going to be run again to install the same packages, but that's not the case when working with containers.docker