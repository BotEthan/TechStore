FROM pypy:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt
COPY . /app
CMD python manage.py runserver