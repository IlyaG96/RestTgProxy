FROM python:3.11.8-slim

WORKDIR /usr/src/rest_tg
COPY requirements.txt /usr/src/rest_tg/

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 10000

ENTRYPOINT ["python"]
CMD ["main.py"]