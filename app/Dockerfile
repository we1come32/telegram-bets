FROM python:3.10

# upgrading and installing system dependens
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt install -y netcat

RUN mkdir /opt/webapp

WORKDIR /opt/webapp

# Environ values
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1

# install requirementsd
COPY requirements.txt ./
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

# coping workdir
COPY src ./

# run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

RUN python ./manage.py migrate
