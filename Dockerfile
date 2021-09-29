## copying a base image from docker hub
FROM python:3.6-alpine
##changing your working directory
WORKDIR /project
## copy local files to project directory
ADD . /
## installing requirements
RUN pip install -r requirements.txt
## Run file
CMD ['python','main3.py']