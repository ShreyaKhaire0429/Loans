FROM python:3.9

WORKDIR /code

COPY requirements.txt .

# RUN pip install -r requirements.txt
RUN pip install -r requirements.txt --default-timeout=100 --no-cache-dir -i https://pypi.org/simple


COPY . .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
