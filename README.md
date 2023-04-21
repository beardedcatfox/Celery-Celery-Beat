# Hillel Celery & Celery Beat
<p>Add a page with a form (do not save anything to the database).
The form should have three fields - email, reminder text, and date/time to receive the reminder.
When the form is submitted, a task is created and deferred to be executed at the time specified in the form, and a reminder is sent to the email specified in the form.</p>

<p> Create a periodic task that will add 5 NEW quotes (and their authors' information) every odd hour. When the quotes run out, send a notification to "yourself" by email that there are no more quotes (to the console).</p>

```
    python manage.py migrate
```
```
    python manage.py makemigrations cel
```
```
    python manage.py sqlmigrate cel 0001
```
```
    python manage.py createsuperuser
```
```bash
    ./manage.py runserver
```
```bash
    celery -A cel worker -B -l INFO
```
