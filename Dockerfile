FROM python:3.6

WORKDIR /app
COPY . .
#RUN apt-get update && apt-get install -y \
#  python3-dev libldap2-dev libsasl2-dev libssl-dev

RUN pip install -r ./requirements.txt
