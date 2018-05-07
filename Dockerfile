FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN mkdir /code
WORKDIR /code
ADD . /code/

#ENV SHELL bash
RUN pip install -U pip
RUN pip install pipenv
#RUN pipenv shell
RUN pipenv install --system

# RUN python3 --version
# RUN python3 manage.py
