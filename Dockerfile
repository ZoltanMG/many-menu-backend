FROM python:3.10.6-slim-bullseye

COPY . /usr/app/src

WORKDIR /usr/app/src


RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

CMD ["python3", "src/app.py"]