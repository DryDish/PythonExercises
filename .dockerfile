# the base image
FROM python:3.8-alpine

# copy all files from dir with Dockerfile and requirements.txt to /app folder in image
COPY ./pip-requirements.txt /

# install python modules
RUN pip install -r requirements.txt

# when container runs it should start in a ash terminal
CMD ["ash"]
