FROM python:3.11:latest

WORKDIR /usr/src/rest_tg
COPY requirements.txt /usr/src/rest_tg/

RUN pip install --no-cache-dir -r requirements.txt
COPY . .


ENTRYPOINT ["python"]
CMD ["main.py"]