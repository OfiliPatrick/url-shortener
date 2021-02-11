# Url-shortener - Shrinkly

Url shortening service built with Flask and SQL.

## Overview

[Shrinkly](https://shrinkly.herokuapp.com/) is a full-stack web application that allows users to convert long URLs to more accessible and maintainable short URLs.

Utilized Flask Rest framework, SQL, and implemented Base62 encoding algorithm for the shortening service.

## Live Demo

Find the live version of the app here: [Shrinkly.com](https://shrinkly.herokuapp.com/)

## Project Structure

---

```sh
├── Procfile
├── README.md
├── .gitignore
├── requirements.txt
├── url_shortener
    ├── static  
    ├── templates
    ├── __init__.py
    ├── auth.py
    ├── extensions.py
    ├── models.py
    ├── routes.py
    ├── settings.py
    └── utils.py
```

## Getting Started

1. Clone the repo

```
$ git clone https://github.com/OfiliPatrick/url-shortener
$ cd url-shortener
```

2. Initialize and activate a virtualenv:

```
$ virtualenv --no-site-packages venv
$ source venv/scripts/activate
```

3. Install the dependencies:

```
$ pip install -r requirements.txt
```

5. Run the development server:

```
$ flask run
```

6. Navigate to [http://localhost:5000](http://localhost:5000)

All configuration is in settings.py.
