# Start from the official Python base image.
FROM python:3.10

# Set the current working directory to /api.
WORKDIR /api

# Copy the file with the requirements to the /api directory.
COPY ./requirements.txt ./requirements.txt

# Install the package dependencies in the requirements file.
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# Copy the ./app directory inside the /api directory.
COPY . /api

EXPOSE 8000

# Set the command to run the uvicorn server.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# The --no-cache-dir option tells pip to not save the downloaded packages locally,as that is only if 
# pip was going to be run again to install the same packages, but that's not the case when working with containers.