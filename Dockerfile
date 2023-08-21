FROM python:3.9

ENV PYTHONUNBUFFERED 1


# Создание и переход в рабочую директорию

WORKDIR /KokocApp/

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app .

#CMD["python","manage.py","createsuperuser"]