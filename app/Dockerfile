FROM python:3.10

# upgrading and installing system dependens
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install postgresql-dev gcc python3-dev musl-dev

WORKDIR /app

# Environ values
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1

# install requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# coping workdir
COPY src ./src

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

CMD ["python3", "./src/manage.py", "migrate"]

CMD ["python3", "./src/manage.py", "runserver", "0.0.0.0:8000"]
