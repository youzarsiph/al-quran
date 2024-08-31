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
mv quran-api quran_api
```

Install dependencies:

```bash
cp quran_api/requirements.txt .
python -m pip install -r requirements.txt
```

Create a Django project:

```bash
python -m django startproject mysite
mv -r quran_api mysite/quran_api
```

Configure the settings, open `mysite/settings.py` in your favorite editor:

```python
...

# Find INSTALLED_APPS setting
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
    # Default apps
    ...
]

...

# Scroll down to the bottom of the file and add the following lines
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 25,
}
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

Open this [page](http://127.0.0.1:8000/) on your browser. Now you are ready to go.

## License

Licensed under MIT License
