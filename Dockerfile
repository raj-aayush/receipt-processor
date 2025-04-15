FROM python:3.9-slim

WORKDIR /src

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app ./app

ENV PYTHONPATH=/src

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]