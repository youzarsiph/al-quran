# quran-api

[![Django CI](https://github.com/youzarsiph/quran-api/actions/workflows/django.yml/badge.svg)](https://github.com/youzarsiph/quran-api/actions/workflows/django.yml)
[![Black](https://github.com/youzarsiph/quran-api/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/quran-api/actions/workflows/black.yml)
[![Ruff](https://github.com/youzarsiph/quran-api/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/quran-api/actions/workflows/ruff.yml)

Quran API endpoints built using Python, Django and DRF.

## Get Started

Open your terminal and follow the steps.

Clone the repo:

```bash
git clone https://github.com/youzarsiph/quran-api
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Create a Django project:

```bash
python -m django startproject mysite
mv quran_api mysite/quran_api
```

Configure the settings, open `mysite/settings.py` in your favorite editor:

```python
INSTALLED_APPS = [
    # Add the following lines
    "quran_api",
    "quran_api.chapters",
    "quran_api.groups",
    "quran_api.pages",
    "quran_api.parts",
    "quran_api.quarters",
    "quran_api.verses",
    # Dependencies
    "drf_redesign",
    "rest_framework",
    "django_filters",
    ...
]
```

Configure URLConf, open `mysite/urls.py`

```python
# Copy and paste the following lines

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("quran_api.urls")),
    path("auth/", include("rest_framework.urls")),
]

```

Run migrations to create database tables:

```bash
cd mysite
python manage.py migrate
```

Create a superuser, run the following command and enter your username and password when prompted:

```bash
python manage.py createsuperuser
```

Run the server on your machine:

```bash
python manage.py runserver
```

## License

Licensed under MIT License
