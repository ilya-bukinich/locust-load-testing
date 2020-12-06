# pull official base image
FROM python:3.7

# set work directory
WORKDIR /usr/src/app

# install dependencies
COPY requirements.txt locustfile.py entrypoint.sh ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
