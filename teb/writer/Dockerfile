# Use an official Python runtime as a parent image
FROM python:3

RUN pip install kafka-python pymongo

ADD task3.py /


# Run app.py when the container launches
CMD ["python", "./task3.py"]