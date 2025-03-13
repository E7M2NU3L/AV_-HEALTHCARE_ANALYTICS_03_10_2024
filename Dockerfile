FROM python:3.7.5

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY models/ /app/

COPY templates/ /app/

COPY static /app/

COPY main.py /app/

EXPOSE 5050

CMD [ "python", "main.py" ]