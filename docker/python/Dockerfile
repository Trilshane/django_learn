FROM python

RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR  /home/sites/
COPY . .

ADD requirements.txt /home/sites/
RUN pip install -r requirements.txt