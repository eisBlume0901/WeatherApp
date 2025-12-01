To clone the repository to your local machine (preferably use pycharm), use the following command:
1. git clone or download the zip file of the repository.
2. cd into the project directory. 
3. Activate the virtual environment:
uv sync - to synchronize the virtual environment with the dependencies listed in the uv.toml file
4. cd to core directory
5. Run the development server: 
python manage.py runserver

uv add django - to add the Django web framework

uv add requests - to add the Requests library for making HTTP requests

uv run django-admin startproject [name_of_your_project] - to create a new Django project

uv add django-environ - to add django-environ for environment variable management

uv add gunicorn - to add Gunicorn as a WSGI HTTP server for deploying Django applications

python manage.py runserver - to start the development server

python manage.py startapp [name_of_your_app] - to create a new Django app within your project

python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' - to generate a new Django secret key