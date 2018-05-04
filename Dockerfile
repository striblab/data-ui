FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
ENV SHELL bash
RUN pip install -U pip
RUN pip install pipenv
#RUN pipenv shell
RUN pipenv install --system
RUN python3 manage.py migrate
RUN python3 manage.py migrate --database "datadrop_business"
RUN python3 manage.py collectstatic --noinput
