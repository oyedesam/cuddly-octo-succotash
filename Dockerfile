FROM python:3.9

ADD init.py .

CMD ["python", "./init.py"]