FROM python:3.10

WORKDIR /task5

COPY . /task5

RUN apt-get update && apt-get install -y libpq-dev
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD [ "gunicorn","task5.wsgi:application","--bind","0.0.0.0:8000" ] 