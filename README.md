# Application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/AlbinaKaybysheva/we_go_trip_tech.git
$ cd we_go_trip_tech
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv ./venv
$ . venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/admin/`.
