

FROM python:3

WORKDIR \app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV set FLASK_APP=server.py

CMD flask run --host=0.0.0.0